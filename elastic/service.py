import json
import os
from elasticsearch import Elasticsearch
from elastic.exceptions import ElasticsearchConfigError


class ElasticsearchService:
    def __init__(self):
        ES_CLUSTER_URL = os.getenv('ES_CLUSTER_URL')
        if ES_CLUSTER_URL is None:
            raise ElasticsearchConfigError('ES Cluster URL not found')

        self.client = Elasticsearch([ES_CLUSTER_URL])

    def ingest(self, index, body):
        """
            Ingest an ElasticSearch document
        """
        if not self.client.indices.exists(index):
            print('\n  --- Index %s does not exist. Creating...\n' % index)
            self.__create_index(index)

        self.client.index(index, body)

    def ping(self):
        """
            Ping
        """
        return self.client.ping()

    def __create_index(self, index):
        with open('elastic/posting_index_mapping.json', 'r') as index_mapping_file:
            index_mapping = json.load(index_mapping_file)

        self.client.indices.create(
            index=index,
            body={'mappings': index_mapping},
        )
