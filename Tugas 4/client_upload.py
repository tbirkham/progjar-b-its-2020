import socket
import sys
import base64

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 8888)
print(sys.stderr, 'connecting to %s port %s' % server_address)

sock.connect(server_address)
message = ("upload filetext.txt")
namafile = "".join(message.split()[1])

f = open(namafile, "rb")
panjangfile = len(namafile) + 1
isi = base64.encodebytes(f.read())
f.close()

f = open("base64encode","wb")
f.write(isi)
f.close()

f = open("base64encode","rb")
msg = message.encode() + (b" ") + f.read(1024)
print(msg)

while (msg):
    sock.send(msg)
    msg = f.read(1024)
    data = sock.recv(1024)

print(message + " Successfully uploaded")
sock.close()