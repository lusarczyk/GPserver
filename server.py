import sys
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import socketserver

if __name__ == "__main__":
    port = 8018
    ipaddr = socket.gethostbyname(socket.gethostname())

    address = (ipaddr,port)

    print("Serwuje: ",ipaddr," port: ",port)

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(address)
    server_socket.listen(5)

    conn, address = server_socket.accept()
    print("Connected to client at ", address)
    # pick a large output buffer size because i dont necessarily know how big the incoming packet is

    chunk = str("")

    while True:
        try:
            output = conn.recv(2048);
        except:
            print("disconnected")
            conn, address = server_socket.accept()
            print("Connected to client at ", address)

        print("Message received from client:")

        print(output)

