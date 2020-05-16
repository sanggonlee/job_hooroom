from elastic.requestor import ElasticsearchRequestor


class ElasticsearchQueryer:
    def __init__(self, query):
        self.requestor = ElasticsearchRequestor()
