from datetime import datetime
import json


class Posting:
    def __init__(
        self,
        title,
        link,
        is_remote,
        company_name,
        location,
        base_location='',
        description='',
        seniority='',
        employment_type='',
        industry=[],
        job_functions=[],
        skills=[],
        words=[],
    ):
        self.title = title
        self.link = link
        self.is_remote = is_remote
        self.company_name = company_name
        self.location = location
        self.base_location = base_location
        self.description = description
        self.seniority = seniority
        self.industry = industry
        self.employment_type = employment_type
        self.job_functions = job_functions
        self.skills = skills
        self.words = words

        self.ingested_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def to_json(self):
        return json.dumps(self.__dict__)
