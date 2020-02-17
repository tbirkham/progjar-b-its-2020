import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
f = open("capture.png", "rb")
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    # Send data
    message = f.read()
    print(f"sending {message}")
    sock.sendall(message)

finally:
    print("closing")
    sock.close()