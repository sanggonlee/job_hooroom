from datetime import datetime
import json
from models.log_segment import LogSegment
from decorators.serializable import serializable


@serializable
class PipelineLog:
    def __init__(self):
        self.logs = []

    def set_started(self):
        self.started_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def set_completed(self, num_processed):
        self.completed_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.num_processed = num_processed

    def add(self, log):
        self.logs.append(log.to_json())
