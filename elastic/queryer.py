from elastic.requestor import ElasticsearchRequestor


class ElasticsearchQueryer:
    """
        ElasticSearch query requestor
        Unlike ingestor, this is intended for single-time use only
    """

    def __init__(self):
        self.requestor = ElasticsearchRequestor()
        self.query = {}

    def filter(self):
        # TODO: Hook up search criteria
        return self

    def aggregation(self, *argv):
        if "aggs" not in self.query:
            self.query["aggs"] = {}

        for term in argv:
            self.query["aggs"][term] = {
                "terms": {
                    "field": term + '.keyword'
                }
            }

        return self

    def execute(self):
        return self.requestor.search(
            # TODO: Hook up search criteria into indices
            indices=[],
            query=self.query,
        )
