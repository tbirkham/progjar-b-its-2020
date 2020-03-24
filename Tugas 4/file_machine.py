import json
import logging
import base64
from handler import Handler

'''
------ PROTOCOL FORMAT ------
String terbagi menjadi 2 bagian yang dipisahkan oleh spasi
------ FITUR ------
1. Mengunggah File (Upload)
   Untuk mengunggah/upload file ke folder 'dir'
   Request : upload
   Parameter : upload namafile
   Respon : jika berhasil, maka akan mengeluarkan tulisan namafile Successfully uploaded
            jika gagal, mengeluarkan tulisan Error
2. Mengunduh File (Download)
   Untuk mengunduh/download file dari dalam folder 'dir'
   Request : download
   Parameter: namafile yg ingin di download dari folder dir
   Response: file yang terdownload akan muncul di direktori script berada
3. Melihat Isi File (List File)
   Untuk melihat list file yang berada dalam folder 'dir'
   Request : list
   Parameter : -
   Response: menampilkan nama-nama file dalam folder 'dir'
Jika command tidak dikenali akan merespon dengan ERRCMD
'''

p = Handler()

class FileMachine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='upload'):
                logging.warning("upload")
                source = cstring[1].strip()
                dest = cstring[2].strip()
                p.upload_file(source,dest.encode())
                return "Ok, File Uploaded"

            elif (command=='download'):
                logging.warning("download")
                source = cstring[1].strip()
                res = p.download_file(source)
                return res[0]

            elif (command=='list'):
                logging.warning("list")
                res = p.list_file()
                dict = {"status":"success","data": res}
                return json.dumps(dict)
            else:
                return "ERRCMD"

        except:
            return "ERROR"

if __name__=='__main__':
    pm = FileMachine()
    run = pm.proses("list")
    print(run)