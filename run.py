#!/usr/bin/python3
import sched , time
import datetime
import config
import connect_ftp
import compressing
#
s = sched.scheduler(time.time , time.sleep)
print("[*] mempersiapkan...")


def main():
    path = "contoh_data_untuk_di_upload/"
    save_to = "tmp/" + (((str(datetime.datetime.now()).replace("-" , "")).replace(" " ,'')).replace(":" ,"")).replace(".","") + ".zip"


    data = compressing.compress(path , save_to)
    file = data.compressing()
    print("[+] file : " + file)
    print("[!] tanggal upload : " + str(datetime.datetime.now()))
    print("[+] persiapan untuk upload")
    configure = config.config()
    print("[?] ceredentials : " + str(configure.setup()))
    send   = connect_ftp.connect(configure.setup())

    send.upload(file)


def test(sc):
    print('ready')
    s.enter(1 , 1 , oke , ("sc" ,))

if __name__ == '__main__':
    s.enter(1 , 1 , main , ())
    s.run()
