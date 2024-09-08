from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random
from urllib.parse import urlparse, parse_qs


class QuoteAPI(BaseHTTPRequestHandler):
    quotes = [
        "The best way to predict the future is to invent it.",
        "Life is 10% what happens to us and 90% how we react to it.",
        "The only way to do great work is to love what you do."
    ]

    def do_GET(self):
        # Choose a random quote
        random_quote = random.choice(self.quotes)

        # Respond with the quote
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        response_data = {"quote": random_quote}
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=QuoteAPI, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting Quote API on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
