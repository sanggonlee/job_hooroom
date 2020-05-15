import os
import sys
import time
from typing import Generator
from helium import *
from models.posting import Posting


def get_url(get_only_last_24_hrs=True, get_only_remote=True):
    url = 'https://www.linkedin.com/jobs/search/?'

    if get_only_last_24_hrs:
        url += 'f_TPR=r86400&'
    if get_only_remote:
        url += 'f_CF=f_WRA&'

    return url


class LinkedinScraper:

    url = get_url()

    def run(self) -> Generator[Posting, None, None]:
        print('===========================================================================================================')
        print('')
        print(' Linkedin scrape starting')
        print('')
        print('     URL: %s' % self.url)
        print('')
        print('===========================================================================================================')

        self.driver = start_chrome(self.url)

        self.__login()

        time.sleep(1)
        listings = find_all(S('li.occludable-update'))
        i = 0
        for listing in listings:
            i += 1
            if i > 4:
                break

            click(listing)
            time.sleep(1)

            if listing.web_element.find_elements_by_xpath(".//span[@class='artdeco-entity-lockup__label']"):
                print('Promoted listing')
                # continue

            is_remote, location = self.__extract_location()
            seniority, employment_type, industry, job_functions = self.__extract_job_attributes()

            yield Posting(
                title=self.__extract_job_title(),
                link=self.__extract_link(),
                is_remote=is_remote,
                company_name=self.__extract_company_name(),
                location=location,
                description=self.__extract_description(),
                seniority=seniority,
                employment_type=employment_type,
                industry=industry,
                job_functions=job_functions,
                skills=self.__extract_skills(),
            )

        print('===========================================================================================================')
        print('')
        print(' Linkedin scrape complete')
        print('')
        print('===========================================================================================================')

    def __login(self):
        LINKEDIN_LOGIN = os.getenv('LINKEDIN_LOGIN')
        LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')

        click('SIGN IN')
        #wait_until(Button('Sign in').exists)
        time.sleep(1)
        write(LINKEDIN_LOGIN, into=S('input#username'))
        time.sleep(0.3)
        write(LINKEDIN_PASSWORD, into='Password')
        press(ENTER)

    def __extract_job_title(self):
        job_titles = self.driver.find_elements_by_xpath(
            "//div[contains(@class, 'jobs-details__main-content')]//h2[contains(@class, 'jobs-details-top-card__job-title')]")
        if not job_titles:
            print('Job title not found!')
        job_title = job_titles[0].text
        return job_title

    def __extract_link(self):
        return self.driver.find_element_by_xpath(
            "//a[contains(@class, 'jobs-details-top-card__job-title-link')]"
        ).get_attribute('href')

    def __extract_company_name(self):
        return self.driver.find_element_by_xpath(
            "//div[contains(@class, 'jobs-details-top-card__company-info')]//a[contains(@data-control-name, 'company_link')]"
        ).text

    def __extract_location(self) -> (bool, str):
        """ Returns is_remote and location """

        job_details_locations = self.driver.find_elements_by_xpath(
            "//div[contains(@class, 'jobs-details-top-card__company-info')]//span[contains(@class, 'jobs-details-top-card__bullet')]"
        )
        if not job_details_locations:
            print('Job details locations not found!')

        location = job_details_locations[-1].text
        # TODO: Handles remote only, revisit when adding on-site
        is_remote = len(
            job_details_locations) > 1 and job_details_locations[0].text == 'Remote'

        return is_remote, location

    def __extract_description(self) -> str:
        return self.driver.find_element_by_xpath(
            "//div[contains(@class, 'jobs-description-content__text')]//span"
        ).text

    def __extract_job_attributes(self) -> (str, str, [str], [str]):
        """ Returns seniority, employment_type, industry, job_funtions """
        job_type_box_elems = self.driver.find_elements_by_xpath(
            "//div[contains(@class, 'jobs-description-details')]//div[contains(@class, 'jobs-box__group')]"
        )
        if not job_type_box_elems:
            print('Job type elements not found!')

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
                print('Unknown job type attribute', attr)

        return seniority, employment_type, industry, job_functions

    def __extract_skills(self) -> [str]:
        skill_elems = self.driver.find_elements_by_xpath(
            "//ul[contains(@class, 'jobs-ppc-criteria__list--skills')]//li//span[contains(@class, 'jobs-ppc-criteria__value')]"
        )
        if not skill_elems:
            print('Skills not found!')

        return [el.text for el in skill_elems]
