import datetime
import os
import zipfile

class compress():

    def __init__(self , path, save_to):
        self.path = path
        self.save_to = save_to

    def zipdir(self,path, ziph):
        # ziph is zipfile handle
        for root, dirs, files in os.walk(path):
            for file in files:
                ziph.write(os.path.join(root, file))

    def compressing(self):
        zipf = zipfile.ZipFile(self.save_to, 'w', zipfile.ZIP_DEFLATED)
        self.zipdir(self.path, zipf)
        zipf.close()
        return self.save_to

#a = compress("../../C" , "tmp/" + (((str(datetime.datetime.now()).replace("-" , "")).replace(" " ,'')).replace(":" ,"")).replace(".","") + ".zip")
#print a.compressing()
