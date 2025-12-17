#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    def _send_text(self, code, message):
        self.send_response(code)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def _send_json(self, code, data):
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        if self.path == "/":
            self._send_text(200, "Hello, this is a simple API!")
        elif self.path == "/data":
            self._send_json(200, {
                "name": "John",
                "age": 30,
                "city": "New York"
            })
        elif self.path == "/status":
            self._send_text(200, "OK")
        elif self.path == "/info":
            self._send_json(200, {
                "version": "1.0",
                "description": "A simple API built with http.server"
            })
        else:
            self._send_text(404, "Endpoint not found")


def run():
    server = HTTPServer(("", 8000), SimpleAPIHandler)
    server.serve_forever()


if __name__ == "__main__":
    run()
