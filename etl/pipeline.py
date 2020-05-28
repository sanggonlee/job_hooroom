from etl.linkedin.scrape import LinkedinScraper
from models.pipeline_log import PipelineLog

DATASOURCE_LINKEDIN = 'linkedin'


class Pipeline:

    extractors = []
    pipes = []
    loggers = []

    def __init__(self, extractors=[], loggers=[]):
        for extractor_key in extractors:
            if extractor_key is DATASOURCE_LINKEDIN:
                self.extractors.append(LinkedinScraper())

        self.loggers = loggers

    def pipe(self, *argv):
        self.pipes = argv

    def run(self):
        pipeline_log = PipelineLog()
        pipeline_log.set_started()

        num_processed = 0
        for posting, log in self.__run_extraction():
            num_processed += 1

            for pipe in self.pipes:
                pipe.process(posting, log)

            if log:
                pipeline_log.add(log)
            print(posting.to_json())

        pipeline_log.set_completed(num_processed)

        for logger in self.loggers:
            logger.log(pipeline_log)

    def __run_extraction(self):
        for extractor in self.extractors:
            for posting, log in extractor.run():
                yield posting, log


class ConsoleLogger:
    def log(self, pipeline_log):
        print(pipeline_log)


class EsLogger:
    def __init__(self, es):
        self.es = es

    def log(self, pipeline_log):
        self.es.ingest(pipeline_log.to_json())
