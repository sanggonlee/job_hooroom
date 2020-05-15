from datetime import datetime
from elastic.service import ElasticsearchService


class Loader:
    def __init__(self):
        self.es = ElasticsearchService()

    def process(self, posting):
        index = 'posting_' + datetime.now().strftime('%Y-%m')

        self.es.ingest(
            index=index,
            body=posting.to_json(),
        )

        return posting
