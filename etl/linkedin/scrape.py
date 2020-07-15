import os
import sys
import time
from datetime import datetime
from typing import Generator, Optional, Tuple
import selenium
from helium import *
from models.log_segment import LogSegment
from models.posting import Posting
from etl.linkedin.enums import Title, Industry

MAX_POSTINGS_PER_PAGE = 25


def get_url(
    get_only_last_24_hrs=True,
    get_only_remote=True,
    get_worldwide=False,
    job_functions=['it'],
    industry=[Industry.ComputerSoftware],
    titles=[
        Title.SoftwareEngineer,
        Title.Developer,
        Title.SeniorSoftwareEngineer,
        Title.WebDeveloper,
        Title.SeniorDeveloper,
        Title.ApplicationDeveloper,
        Title.FrontendDeveloper,
        Title.FrontendEngineer,
        Title.BackEndDeveloper,
    ],
):
    url = 'https://www.linkedin.com/jobs/search?'
    filters = []

    if get_worldwide:
        filters.append('location=Worldwide')
    if get_only_last_24_hrs:
        filters.append('f_TPR=r86400')
    if get_only_remote:
        filters.append('f_CF=f_WRA')
    if len(job_functions) > 0:
        filters.append('f_F=' + '%2C'.join(job_functions))
    if len(industry) > 0:
        filters.append(
            'f_I=' + '%2C'.join([str(ind.value) for ind in industry]))
    if len(titles) > 0:
        filters.append(
            'f_T=' + '%2C'.join([str(title.value) for title in titles]))

    return url + '&'.join(filters)


class LinkedinScraper:

    url = get_url(
        get_only_remote=False,
        industry=[],
        job_functions=[],
    )

    def run(self) -> Generator[Tuple[Posting, Optional[LogSegment]], None, None]:
        print('===========================================================================================================')
        print('')
        print(' Linkedin scrape starting')
        print('')
        print('     Started: %s' %
              datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        print('     URL: %s' % self.url)
        print('')
        print('===========================================================================================================')

        self.driver = start_chrome(self.url, headless=True)

        self.__login()

        time.sleep(3)

        retry_count = 0
        curr_offset = 0

        while True:
            if retry_count > 4:
                print('Retry count exceeded. Exiting...')
                break

            listings = self.driver.find_elements_by_xpath(
                "//li[contains(@class, 'occludable-update')]")

            if len(listings) == 0:
                break

            try:
                for posting, log in self.__process_listings(listings):
                    curr_offset += 1
                    yield posting, log
            except selenium.common.exceptions.StaleElementReferenceException:
                retry_count += 1
                print('Retrying... count:' + str(retry_count))

            go_to(self.url + '&start=' + str(curr_offset))
            time.sleep(5)

        print('===========================================================================================================')
        print('')
        print(' Linkedin scrape complete')
        print('')
        print('===========================================================================================================')

    def __login(self):
        LINKEDIN_LOGIN = os.getenv('LINKEDIN_LOGIN')
        LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')

        click('SIGN IN')
        # wait_until(Button('Sign in').exists)
        time.sleep(1)
        write(LINKEDIN_LOGIN, into=S('input#username'))
        time.sleep(0.3)
        write(LINKEDIN_PASSWORD, into='Password')
        press(ENTER)

    def __process_listings(self, listings):
        for listing in listings:

            # Click on the corner to avoid clicking company (which is a link)
            action = selenium.webdriver.common.action_chains.ActionChains(
                self.driver)
            action.move_to_element_with_offset(listing, 5, 5)
            action.click()
            action.perform()

            time.sleep(0.5)

            # if listing.web_element.find_elements_by_xpath(".//span[@class='artdeco-entity-lockup__label']"):
            #     print('Promoted listing')
            #     # continue

            errors = []
            messages = []

            title = self.__extract_job_title(errors, messages)
            link = self.__extract_link(errors, messages)
            is_remote, location = self.__extract_location(
                errors, messages)
            company_name = self.__extract_company_name(
                errors, messages)
            description = self.__extract_description(
                errors, messages)
            seniority, employment_type, industry, job_functions = self.__extract_job_attributes(
                errors, messages)
            skills = self.__extract_skills(errors, messages)

            log = None if not errors and not messages else LogSegment(
                status='failure' if errors else 'success',
                errors=errors,
                messages=messages,
            )

            yield Posting(
                title=title,
                link=link,
                is_remote=is_remote,
                company_name=company_name,
                location=location,
                description=description,
                seniority=seniority,
                employment_type=employment_type,
                industry=industry,
                job_functions=job_functions,
                skills=skills,
            ), log

    def __extract_job_title(self, errors, messages) -> str:
        job_titles = self.driver.find_elements_by_xpath(
            "//div[contains(@class, 'jobs-details__main-content')]//h2[contains(@class, 'jobs-details-top-card__job-title')]")
        if not job_titles:
            errors.append('Job title elements not found')
            return ''

        job_title = job_titles[0].text
        return job_title

    def __extract_link(self, errors, messages) -> str:
        links = self.driver.find_elements_by_xpath(
            "//a[contains(@class, 'jobs-details-top-card__job-title-link')]"
        )
        if not links:
            messages.append('Link elements not found')
            return ''

        return links[0].get_attribute('href')

    def __extract_company_name(self, errors, messages) -> str:
        elems = self.driver.find_elements_by_xpath(
            "//div[contains(@class, 'jobs-details-top-card__company-info')]//a[contains(@data-control-name, 'company_link')]"
        )
        if elems:
            return elems[0].text

        elems = self.driver.find_elements_by_xpath(
            "//div[contains(@class, 'jobs-details-top-card__company-info')]"
        )
        if elems:
            return elems[0].text

        messages.append('Company name not found')
        return ''

    def __extract_location(self, errors, messages) -> (bool, str):
        """ Returns is_remote and location """

        job_details_locations = self.driver.find_elements_by_xpath(
            "//div[contains(@class, 'jobs-details-top-card__company-info')]//span[contains(@class, 'jobs-details-top-card__bullet')]"
        )

        if job_details_locations:
            location = job_details_locations[-1].text
            is_remote = len(
                job_details_locations
            ) > 1 and job_details_locations[0].text == 'Remote'
            return is_remote, location

        job_details_locations = self.driver.find_elements_by_xpath(
            "//div[contains(@class, 'jobs-details-top-card__company-info')]//a[contains(@class, 'jobs-details-top-card__exact-location')]"
        )
        if not job_details_locations:
            messages.append('Job details locations not found')
            return False, ''

        location = job_details_locations[0].text
        return False, location

    def __extract_description(self, errors, messages) -> str:
        elems = self.driver.find_elements_by_xpath(
            "//div[contains(@class, 'jobs-description-content__text')]//span"
        )
        if not elems:
            messages.append('Job description not found')
            return ''

        return elems[0].text

    def __extract_job_attributes(self, errors, messages) -> (str, str, [str], [str]):
        """ Returns seniority, employment_type, industry, job_funtions """
        job_type_box_elems = self.driver.find_elements_by_xpath(
            "//div[contains(@class, 'jobs-description-details')]//div[contains(@class, 'jobs-box__group')]"
        )
        if not job_type_box_elems:
            messages.append('Job type elements not found')
            return '', '', [], []

        def extract_text_list(el) -> [str]:
            return [e.text for e in el.find_elements_by_xpath('.//ul//li')]

        seniority = ''
        employment_type = ''
        industry = []
        job_functions = []
        for elem in job_type_box_elems:
            attr = elem.find_element_by_tag_name('h3').text
            if attr == 'Seniority Level':
                seniority = elem.find_element_by_xpath('.//p').text
            elif attr == 'Industry':
                industry = extract_text_list(elem)
            elif attr == 'Employment Type':
                employment_type = elem.find_element_by_xpath('.//p').text
            elif attr == 'Job Functions':
                job_functions = extract_text_list(elem)
            else:
                errors.append('Unknown job type attribute: %s' % attr)

        return seniority, employment_type, industry, job_functions

    def __extract_skills(self, errors, messages) -> [str]:
        skill_elems = self.driver.find_elements_by_xpath(
            "//ul[contains(@class, 'jobs-ppc-criteria__list--skills')]//li//span[contains(@class, 'jobs-ppc-criteria__value')]"
        )
        if not skill_elems:
            messages.append('Skills not found')
            return []

        return [el.text for el in skill_elems]
