import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket


ipaddr = socket.gethostbyname(socket.gethostname())

class Serv(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        self.wfile.write("<html><body><h1>hi!</h1></body></html>".encode('utf-8'))

    def do_HEAD(self):
        self._set_response()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_response()
        self.wfile.write("<html><body><h1>POST!</h1></body></html>".encode('utf-8'))
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        print("post ::: "+str(self.data_string))


if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8018
server_address = (ipaddr, port)

Serv.protocol_version = "HTTP/1.0"
httpd = HTTPServer(server_address, Serv)

sa = httpd.socket.getsockname()
print("Serving HTTP on", sa[0], "port", sa[1], "...")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    pass

httpd.server_close()
print('Stopping httpd...\n')