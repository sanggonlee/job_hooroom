from typing import Optional
from elastic.doctype import DocType
from elastic.ingestor import PostingIngestor
from elastic.queryer import ElasticsearchQueryer
from models.log_segment import LogSegment
from models.search import Search


class Loader:
    def __init__(self):
        self.ingestor = PostingIngestor()

    def process(self, posting, log: Optional[LogSegment]):
        search = Search(
            queries={},
            title=[posting.title],
            company_name=[posting.company_name],
            link=[posting.link],
        )

        query_result = ElasticsearchQueryer(should_log=False).postings().filter(
            search
        ).limit(1).execute()

        if query_result["hits"]["total"]["value"] > 0:
            print('Skipping duplicate')
            return

        data = posting.to_json()
        resp = self.ingestor.ingest(data)

        if 'result' not in resp or resp['result'] != 'created':
            if not log:
                log = LogSegment()

            log.data = data
            log.status = 'failure'
            log.errors.append('Ingest failed')

        if log and '_id' in resp:
            log.doc_id = resp['_id']
