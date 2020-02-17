import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 31000)
f = input("Input nama file yang ingin dikirimkan : ")
f = f.strip("\n")
print(f"connecting to {server_address}")
sock.connect(server_address)

try:
    # Send data
    message = f
    print(f"sending {message}")
    sock.sendall(message.encode())
    while True:
        data = sock.recv(1024)
        newfile = open("new" + message, 'a+b')
        if not data:
            newfile.close()
            break
        newfile.write(data)

finally:
    print("closing")
    sock.close()