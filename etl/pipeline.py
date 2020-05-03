from etl.linkedin.scrape import LinkedinScraper

DATASOURCE_LINKEDIN = 'linkedin'


class Pipeline:

    extractors = []
    pipes = []

    def __init__(self, extractors=[]):
        for extractor_key in extractors:
            if extractor_key is DATASOURCE_LINKEDIN:
                self.extractors.append(LinkedinScraper())

    def pipe(self, *argv):
        self.pipes = argv

    def run(self):
        for posting in self.__run_extraction():
            for pipe in self.pipes:
                pipe.process(posting)

    def __run_extraction(self):
        for extractor in self.extractors:
            for posting in extractor.run():
                yield posting
