import socket
import sys
import base64
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8888)
print(sys.stderr, 'connecting to %s port %s' % server_address)
sock.connect(server_address)

filedownload = 'perry.jpg'
print(filedownload.encode())
req = (b'download '+filedownload.encode())
print('Downloading file '+ filedownload)

f = open(filedownload,'wb')
file = (b'')
sock.send(req)
data = sock.recv(1024)

while 1:
    file += data
    print(data)
    if sys.getsizeof(data) != 1057:
        break
    else:
        data = sock.recv(1024)

file = base64.decodebytes(file)
f.write(file)
f.close()

print(filedownload+" Successfully downloaded")
sock.close()