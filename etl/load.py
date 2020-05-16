from datetime import datetime
from elastic.doctype import DocType
from elastic.ingestor import PostingIngestor


class Loader:
    def __init__(self):
        self.es = PostingIngestor()

    def process(self, posting):
        self.es.ingest(posting.to_json())

        return posting
