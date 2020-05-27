from typing import Optional
from elastic.doctype import DocType
from elastic.ingestor import PostingIngestor
from models.log_segment import LogSegment


class Loader:
    def __init__(self):
        self.es = PostingIngestor()

    def process(self, posting, log: Optional[LogSegment]):
        data = posting.to_json()
        resp = self.es.ingest(data)

        if 'result' not in resp or resp['result'] != 'created':
            if not log:
                log = LogSegment()

            log.data = data
            log.status = 'failure'
            log.errors.append('Ingest failed')

        if log and '_id' in resp:
            log.doc_id = resp['_id']
