import sys
import socket
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('127.0.0.1', 31000)
print(f"starting up on {server_address}")
sock.bind(server_address)
# Listen for incoming connections
sock.listen(1)
while True:
    # Wait for a connection
    print("waiting for a connection")
    connection, client_address = sock.accept()
    print(f"connection from {client_address}")
    # Receive the data in small chunks and retransmit it
    while True:
        data = connection.recv(1024)
        a = "newfile"
        b = ".png"
        newfile = open(a + b, 'a+b')
        if not data:
            newfile.close()
            break
        newfile.write(data)
    connection.close()