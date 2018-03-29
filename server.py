import sys
import BaseHTTPServer
import socket


ipaddr = socket.gethostbyname(socket.gethostname())

class S(BaseHTTPServer.BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>")

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>")


if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8018
server_address = (ipaddr, port)

S.protocol_version = "HTTP/1.0"
httpd = BaseHTTPServer.HTTPServer(server_address, S)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."
httpd.serve_forever()