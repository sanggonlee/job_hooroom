from datetime import datetime
import json
from elastic.doctype import DocType
from elastic.errors import UnknownDocTypeError
from elastic.requestor import ElasticsearchRequestor


class ElasticsearchIngestor():
    """
        ElasticsearchIngestor is a reusable, index-scope ElasticSearch ingest requestor
    """

    def __init__(self, doctype: DocType):
        self.requestor = ElasticsearchRequestor()
        self.doctype = doctype
        self.index = self.__get_index(doctype)

        if not self.requestor.index_exists(self.index):
            print('\n  --- Index %s does not exist. Creating...\n' % self.index)
            self.__create_index(self.index)

    def ingest(self, body):
        """
            Ingest an ElasticSearch document
        """
        self.requestor.ingest(self.index, body)

    def __get_index(self, doctype: DocType):
        if doctype is DocType.Posting:
            return 'posting_' + datetime.now().strftime('%Y-%m')
        else:
            raise UnknownDocTypeError(type, 'when computing index')

    def __create_index(self, index):
        mapping_file = None
        if self.doctype is DocType.Posting:
            mapping_file = 'elastic/posting_index_mapping.json'

        if mapping_file is None:
            raise UnknownDocTypeError(
                self.doctype, 'when trying to create index')

        with open(mapping_file, 'r') as f:
            index_mapping = json.load(f)

        return self.requestor.index_create(index, index_mapping)
