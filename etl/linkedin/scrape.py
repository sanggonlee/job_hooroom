import os
import sys
import time
from helium import *


def get_url(get_only_last_24_hrs=True, get_only_remote=True):
    url = 'https://www.linkedin.com/jobs/search/?'

    if get_only_last_24_hrs:
        url += 'f_TPR=r86400&'
    if get_only_remote:
        url += 'f_CF=f_WRA&'

    return url


class LinkedinScraper:

    url = get_url()

    def run(self):
        print('Scraping')
        print(hasattr(sys, 'real_prefix'))

        self.driver = start_chrome(self.url)

        self.__login()

        listings = find_all(S('li.occludable-update'))
        print(listings)
        i = 0
        for listing in listings:
            i += 1
            if i > 4:
                break

            print(listing.web_element)

            click(listing)
            time.sleep(0.5)

            if listing.web_element.find_elements_by_xpath(".//span[@class='artdeco-entity-lockup__label']"):
                print('Promoted listing')
                # continue

            job_title = self.__extract_job_title()
            print(job_title)

            job_details_company_name = self.__extract_company_name()
            print(job_details_company_name)

            job_location = self.__extract_location()
            print(job_location)

            yield job_title

    def __login(self):
        LINKEDIN_LOGIN = os.getenv('LINKEDIN_LOGIN')
        LINKEDIN_PASSWORD = os.getenv('LINKEDIN_PASSWORD')

        click('SIGN IN')
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

    def __extract_company_name(self):
        return self.driver.find_element_by_xpath(
            "//div[contains(@class, 'jobs-details-top-card__company-info')]//a[contains(@data-control-name, 'company_link')]"
        ).text

    def __extract_location(self):
        job_details_locations = self.driver.find_elements_by_xpath(
            "//div[contains(@class, 'jobs-details-top-card__company-info')]//span[contains(@class, 'jobs-details-top-card__bullet')]"
        )
        if not job_details_locations:
            print('Job details locations not found!')

        # TODO: Handles remote only, revisit when adding on-site
        return job_details_locations[-1].text
