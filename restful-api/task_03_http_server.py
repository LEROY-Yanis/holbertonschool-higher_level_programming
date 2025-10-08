#!/usr/bin/python

import http.server
import json


class MyHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b"yes")

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"404 Not Found")


def run(port=8080):

    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, MyHandler)
    print(f'Starting httpd server on port {port}...')
    print(f"Access it at: http://localhost:{port}")
    print("\nAvailable endpoints:")
    print(f"  - http://localhost:{port}/")
    print(f"  - http://localhost:{port}/data")
    print(f"  - http://localhost:{port}/status")

    try:
        httpd.serve_forever()

    except KeyboardInterrupt:
        print("\n\nServer stopping.")
        httpd.server_close()


if __name__ == "__main__":
    run()
