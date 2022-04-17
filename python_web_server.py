#!/usr/bin/env python
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer


class HTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        # Send response status code
        self.send_response(200)
        print("Recevied the following headers ")
        print(self.headers)
        print("Sending it back to the caller... ")

        # Send message back to client
        message = bytes(str(self.headers) + "\n" + self.requestline + "\n", "utf8")
        # Send headers
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.send_header("Content-length", str(len(message)))
        self.end_headers()

        # Write content as utf-8 data
        self.wfile.write(message)
        return


def run():
    PORT = int(sys.argv[1]) or 8081
    server_address = ("127.0.0.1", PORT)
    httpd = HTTPServer(server_address, HTTPServer_RequestHandler)
    print(f"running server at {PORT}")
    httpd.serve_forever()


run()
