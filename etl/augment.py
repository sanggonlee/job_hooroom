from typing import Optional
from models.log_segment import LogSegment


class Augmentor:
    def process(self, posting, log: Optional[LogSegment]):
        # Set is_remote to true if title or location contains "remote"
        posting.is_remote = posting.is_remote or (
            'remote' in posting.title.lower()
        ) or (
            'remote' in posting.location.lower()
        )

        # Copy location to base location
        if posting.base_location is '':
            posting.base_location = posting.location

        # Set location to remote if remote
        if posting.is_remote:
            posting.location = 'Remote'

        # For now, simply copy all the keywords to words
        # TODO: Make this more meaningful
        posting.words = [
            posting.location,
            posting.seniority,
            posting.employment_type,
        ] + posting.industry + posting.job_functions + posting.skills
