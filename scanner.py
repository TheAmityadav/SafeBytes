import hashlib
import sys
import sqlite3

class Scanner():

    def __init__(self,db_path,buffer_size=65535):
        self.DB = db_path
        self.buff_size = buffer_size
        self.file_name = None


    def get_file_hash(self,file):
        md5 = hashlib.md5()
        with open(file,'rb') as f:
            while chunk := f.read(self.buff_size):
                md5.update(chunk)

        return md5.hexdigest()


    def check_hash_in_DB(self,md5hash):
        conn = sqlite3.connect(self.DB)
        cursor = conn.cursor()
        cursor.execute("SELECT 1 FROM avhash WHERE hash == (?)",(md5hash,))
        result = cursor.fetchone()

        if result:
            print (True,"Malware found")
        else:
            print (False,"Malware not found")
        cursor.close()
        conn.close()
    



