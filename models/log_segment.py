import json
from decorators.serializable import serializable


@serializable
class LogSegment:
    def __init__(self, status, errors=[], messages=[]):
        self.doc_id = ''
        self.data = None
        self.status = status
        self.errors = errors
        self.messages = messages
