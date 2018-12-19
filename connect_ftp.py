import ftplib
import config

class connect:

    def __init__(self , data):
        self.host     = data['HOST']
        self.username = data['USERNAME']
        self.password = data['PASSWORD']
        self.port     = data['PORT']

    def upload(self , path_file):
        print("[*] preparing untuk upload data")
        session = ftplib.FTP(self.host ,self.username , self.password)
        file = open(path_file,'rb')
        session.storbinary("STOR " + str(path_file) , file )
        print("[+] uploaded")
        file.close()
        session.quit()
