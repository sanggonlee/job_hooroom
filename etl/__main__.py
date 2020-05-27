from etl.pipeline import Pipeline, ConsoleLogger, EsLogger, DATASOURCE_LINKEDIN
from etl.augment import Augmentor
from etl.load import Loader
from elastic.ingestor import LogIngestor

pipeline = Pipeline(
    extractors=[
        DATASOURCE_LINKEDIN,
    ],
    loggers=[
        ConsoleLogger(),
        EsLogger(LogIngestor()),
    ]
)
pipeline.pipe(
    Augmentor(),
    Loader()
)
pipeline.run()
