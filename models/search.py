class Search():
    def __init__(self, queries):
        self.is_remote = None
        if 'is_remote' in queries:
            self.is_remote = queries['is_remote']

        self.location = None
        if 'location' in queries:
            self.location = queries['location']

        self.seniority = None
        if 'seniority' in queries:
            self.seniority = queries['seniority']

        self.industry = None
        if 'industry' in queries:
            self.industry = queries['industry']

        self.employment_type = None
        if 'employment_type' in queries:
            self.employment_type = queries['employment_type']

        self.job_functions = None
        if 'job_functions' in queries:
            self.job_functions = queries['job_functions']

        self.skills = None
        if 'skills' in queries:
            self.job_functions = queries['skills']
