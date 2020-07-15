from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime
from urllib.parse import urlparse, parse_qs
from elastic.queryer import ElasticsearchQueryer
from models.search import Search


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        queries = parse_qs(urlparse(self.path).query)

        search = Search(queries)

        result = ElasticsearchQueryer().postings().filter(
            search
        ).limit(
            0
        ).aggregation(
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

        resp_body = result["aggregations"]

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(resp_body).encode('utf-8'))
        return
