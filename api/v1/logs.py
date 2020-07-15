from http.server import BaseHTTPRequestHandler
import json
from elastic.queryer import ElasticsearchQueryer


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        result = ElasticsearchQueryer().logs().all().execute(include_source=True)

        hits_result = result["hits"]

        resp_body = {
            "total": hits_result["total"]["value"],
            "hits": [hit["_source"] for hit in hits_result["hits"]],
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(resp_body).encode('utf-8'))
        return
