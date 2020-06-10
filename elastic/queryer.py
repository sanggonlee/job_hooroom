from enum import Enum
from typing import Callable, List
from elastic.requestor import ElasticsearchRequestor
from models.search import Search


class BoolJoiner(Enum):
    And = 1
    Or = 2


class FilterCriterion:
    def __init__(self, key: str, accessor: Callable[[Search], List], joiner: BoolJoiner):
        self.key = key
        self.accessor = accessor
        self.joiner = joiner


class ElasticsearchQueryer:
    """
        ElasticSearch query requestor
        Unlike ingestor, this is intended for single-time use only
    """

    criteria = [
        FilterCriterion(
            key='is_remote',
            accessor=lambda s: s.is_remote,
            joiner=BoolJoiner.Or,
        ),
        FilterCriterion(
            key='location',
            accessor=lambda s: s.location,
            joiner=BoolJoiner.Or,
        ),
        FilterCriterion(
            key='seniority',
            accessor=lambda s: s.seniority,
            joiner=BoolJoiner.Or,
        ),
        FilterCriterion(
            key='employment_type',
            accessor=lambda s: s.employment_type,
            joiner=BoolJoiner.Or,
        ),
        FilterCriterion(
            key='industry',
            accessor=lambda s: s.industry,
            joiner=BoolJoiner.And,
        ),
        FilterCriterion(
            key='job_functions',
            accessor=lambda s: s.job_functions,
            joiner=BoolJoiner.And,
        ),
        FilterCriterion(
            key='skills',
            accessor=lambda s: s.skills,
            joiner=BoolJoiner.And,
        ),
    ]

    def __init__(self):
        self.requestor = ElasticsearchRequestor()
        self.query = {}

    def filter(self, search: Search):
        self.query["query"] = {
            "bool": {}
        }

        filters = []
        for criterion in self.criteria:
            add_filter(
                filters,
                criterion.key,
                criterion.accessor(search),
                criterion.joiner,
            )

        if filters:
            self.query["query"]["bool"]["must"] = filters

        return self

    def aggregation(self, *argv):
        if "aggs" not in self.query:
            self.query["aggs"] = {}

        for term in argv:
            field = term
            if field is not 'is_remote':
                field += '.keyword'

            self.query["aggs"][term] = {
                "terms": {
                    "field": field
                }
            }

        return self

    def limit(self, limit):
        self.query["size"] = limit
        return self

    def offset(self, offset):
        self.query["from"] = offset
        return self

    def execute(self, include_source=False):
        print(self.query)
        return self.requestor.search(
            # TODO: Hook up search criteria into indices
            indices=[],
            query=self.query,
            include_source=include_source,
        )


def add_filter(filters: List, key: str, values: List, joiner: BoolJoiner):
    if not values:
        return

    if len(values) is 1:
        add_predicate(filters, key, values[0])
        return

    if joiner is BoolJoiner.And:
        add_and_pred(filters, key, values)
        return

    if joiner is BoolJoiner.Or:
        add_or_pred(filters, key, values)
        return

    raise RuntimeError('Unexpected bool joiner given for filter')


def add_predicate(filters: List, key: str, value: str):
    clause = {}
    clause[key] = value
    filters.append({
        "match": clause
    })


def add_or_pred(filters: List, key: str, values: List):
    clause = {
        "bool": {
            "should": []
        }
    }
    for value in values:
        subclause = {}
        subclause[key] = value
        clause["bool"]["should"].append({
            "match": subclause
        })

    filters.append(clause)


def add_and_pred(filters: List, key: str, values: List):
    for value in values:
        clause = {}
        clause[key] = value
        filters.append({
            "match": clause
        })
