import logging
import requests
import os
import threading



def download_gambar(url=None,i=None):
    if (url is None):
        logging.warning("error")
        return False
    ff = requests.get(url)
    tipe = dict()
    tipe['image/png']='png'
    tipe['image/jpg']='jpg'
    tipe['image/jpeg']='jpg'

    content_type = ff.headers['Content-Type']
    logging.warning(content_type)
    if (content_type in list(tipe.keys())):
        namafile = os.path.basename(url)
        ekstensi = tipe[content_type]
        logging.warning(f"writing {namafile}.{ekstensi} thread {i}")
        fp = open(f"{namafile}.{ekstensi}","wb")
        fp.write(ff.content)
        fp.close()
    else:
        return False


if __name__=='__main__':
    threads = []
    for i in range(3):
        logging.warning(f"Thread {i}")
        t = threading.Thread(target=download_gambar, args=('https://lh3.googleusercontent.com/proxy/lC-VezO-eNLJvgQi_Ooasmx3wTx_94XKsw7JbtEYr9-1WZLVynUAAx3smf58LwCe5n9soKrNGpt0mW3gwHmcRg8Mc1RFxfrIhb9nsOILOEFgYVNhe6UljER9',i,))
        threads.append(t)

    for thr in threads:
        logging.warning(f"{thr} started")
        thr.start()
