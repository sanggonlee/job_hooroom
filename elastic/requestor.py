import certifi
import json
import os
from elasticsearch import Elasticsearch
from elastic.errors import ConfigError


class ElasticsearchRequestor:
    def __init__(self):
        ES_CLUSTER_URL = os.getenv('ES_CLUSTER_URL')
        if ES_CLUSTER_URL is None:
            raise ConfigError('ES Cluster URL not found')

        self.client = Elasticsearch(
            [ES_CLUSTER_URL],
            use_ssl=True,
            ca_certs=certifi.where()
        )

    def index_exists(self, index):
        """
            Checks if an index already exists. Returns True if exists, False otherwise
        """
        return self.client.indices.exists(index)

    def index_create(self, index, mapping):
        """
            Create a new index
        """
        return self.client.indices.create(
            index=index,
            body={'mappings': mapping},
        )

    def ingest(self, index, body):
        """
            Ingest an ElasticSearch document
        """
        return self.client.index(
            index=index,
            body=body,
        )

    def search(self, indices=[], query={}, include_source=False):
        return self.client.search(
            index=','.join(indices),
            body=query,
            _source=include_source,
        )

    def ping(self):
        """
            Ping
        """
        return self.client.ping()
