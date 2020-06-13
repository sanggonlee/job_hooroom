from datetime import datetime
import json
from models.log_segment import LogSegment
from decorators.serializable import serializable


@serializable
class PipelineLog:
    def __init__(self):
        self.logs = []

        # You might be confused why we're storing doc type in doc source,
        # instead of ES doc_type.
        # ES doc_type is misleading and has been removed in future releases
        # but we probably still want to filter by doc types, although the
        # current plan is to store only a single doc types per index.
        # This is a safe and intuitive workaround.
        self.doctype = 'pipeline_log'

    def set_started(self):
        self.started_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def set_completed(self, num_processed):
        self.completed_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.num_processed = num_processed

    def add(self, log):
        self.logs.append(log.to_json())
