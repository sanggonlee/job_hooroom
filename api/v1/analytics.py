from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime
from elastic.queryer import ElasticsearchQueryer


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        result = ElasticsearchQueryer().aggregation(
            'is_remote',
            'location',
            'base_location',
            'seniority',
            'industry',
            'employment_type',
            'job_functions',
            'skills',
            'words',
        ).execute()
        print(result)

        resp_body = result["aggregations"]

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(resp_body).encode('utf-8'))
        return
