import socket
import time

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5006

nama = "Tubagus Irkham"
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(nama.encode()),(TARGET_IP, TARGET_PORT))