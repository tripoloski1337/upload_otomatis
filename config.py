import ftplib
class config:

    def setup(self):
        ftp = ftplib.FTP()
        HOST = ""
        PORT = 22
        USERNAME = ""
        PASSWORD = ""
        print("[*] mengautentikasikan..")
        try:
            ftp.connect(HOST, PORT)
            print(ftp.getwelcome())
            print("[!] terhubung")
            ftp.login(USERNAME,PASSWORD)
            data = {"HOST":HOST,"USERNAME":USERNAME , "PASSWORD":PASSWORD , "PORT":PORT}
            return data
        except ftplib.Error:
            print("[!] gagal login")
            print("[!] error : " + str(ftplib.all_errors))
            #exit(1)
#a = config()
#print a.setup()
