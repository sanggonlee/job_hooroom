from datetime import datetime
from elastic.doctype import DocType
from elastic.ingestor import ElasticsearchIngestor


class Loader:
    def __init__(self):
        self.es = ElasticsearchIngestor(doctype=DocType.Posting)

    def process(self, posting):
        self.es.ingest(posting.to_json())

        return posting
