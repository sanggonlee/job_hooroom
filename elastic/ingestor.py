from datetime import datetime
import json
from elastic.doctype import DocType
from elastic.errors import UnknownDocTypeError
from elastic.requestor import ElasticsearchRequestor


class ElasticsearchIngestor():
    """
        ElasticsearchIngestor is a reusable, index-scope ElasticSearch ingest requestor
        Meant to be used as a base class for more specialized ingestors
    """

    def __init__(self):
        self.requestor = ElasticsearchRequestor()
        self.index = self._get_index()

        # Bonsai doesn't let us use auto-create index, so have to do this for now
        if not self.requestor.index_exists(self.index):
            print('\n  --- Index %s does not exist. Creating...\n' % self.index)
            self._create_index(self.index)

    def ingest(self, body):
        """
            Ingest an ElasticSearch document
        """
        return self.requestor.ingest(
            index=self.index,
            body=body,
        )

    def _create_index(self, index):
        with open(self._get_index_mapping_filename(), 'r') as f:
            index_mapping = json.load(f)

        return self.requestor.index_create(
            index=index,
            mapping=index_mapping,
        )

    def _get_index(self):
        # Implement
        pass

    def _get_index_mapping_filename(self):
        # Implement
        pass


class PostingIngestor(ElasticsearchIngestor):
    def __init__(self):
        self.doctype = DocType.Posting
        super().__init__()

    def _get_index(self):
        return 'posting_' + datetime.now().strftime('%Y-%m')

    def _get_index_mapping_filename(self):
        return 'elastic/posting_index_mapping.json'


class LogIngestor(ElasticsearchIngestor):
    def __init(self):
        self.doctype = DocType.PipelineLog
        super().__init__()

    def _get_index(self):
        return 'log_' + datetime.now().strftime('%Y')

    def _get_index_mapping_filename(self):
        return 'elastic/log_index_mapping.json'
