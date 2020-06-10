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

        limit = 10
        if 'limit' in queries and queries['limit'] and queries['limit'][0].isdigit():
            limit = int(queries['limit'][0])

        offset = 0
        if 'offset' in queries and queries['offset'] and queries['offset'][0].isdigit():
            offset = int(queries['offset'][0])

        result = ElasticsearchQueryer().filter(
            search
        ).limit(
            limit
        ).offset(
            offset
        ).execute(include_source=True)

        print(result)

        # TODO: detect possible key errors

        resp_body = {
            "total": result["hits"]["total"]["value"],
            "hits": [hit["_source"] for hit in result["hits"]["hits"]],
        }

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(resp_body).encode('utf-8'))
        return
