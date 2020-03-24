import shelve
import uuid
import socket
import os
import base64

class Handler:
    def __init__(self):
        # buat folder penyimpanan
        if not os.path.exists('dir'):
            os.makedirs('dir')

    def upload_file(self,nama=None,file=None):
       # cek nama file
        data_file = file
        print(base64.decodestring(data_file))
        f = open("dir/"+nama,"wb")
        f.write(base64.decodestring(data_file))
        return True

    def download_file(self,nama=None):
        tmp = []
        f = open("dir/" + nama,"rb")
        rd = f.read()
        f.close()

        res = base64.encodestring(rd)
        tmp.append(res.decode())
        return tmp

    def list_file(self):
        isi = os.listdir("dir")
        tmp = []
        for fname in isi:
            tmp.append(fname)
        return tmp

if __name__=='__main__':
    handler = Handler()
    print(handler.list_file())