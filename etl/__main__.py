from etl.pipeline import Pipeline, DATASOURCE_LINKEDIN
from etl.augment import Augmentor
from etl.load import Loader

pipeline = Pipeline([DATASOURCE_LINKEDIN])
pipeline.pipe(
    Augmentor(),
    Loader()
)
pipeline.run()
