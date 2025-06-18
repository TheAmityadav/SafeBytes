#!/usr/bin/python

import os
import sys
import time

from colorama import Fore, Style, init
init(autoreset=True)
import sqlite3
from scanner import Scanner
from fetch_hash import fetch_hash_from_virush_share


DB = 'hash.db'
scanner_obj = Scanner(db_path=DB)

def scan_file(file_name):
    try:
        print(f"{Fore.CYAN}Staring scanning {file_name}")
        md5hex = scanner_obj.get_file_hash(file=file_name)
        status,err_msg = scanner_obj.check_hash_in_DB(md5hash=md5hex)
        if status:
            print (f"{Fore.RED}Malware Detected in file {file_name}")
        else:
            print (f"{Fore.GREEN}No malware found in {file_name}")
    except Exception as e:
        print(f"{Fore.RED}Error starting to scan the file",{e})

def update_hash():
    print (f"{Fore.CYAN}Starting to update the hash ..")
    status,err_msg = fetch_hash_from_virush_share()
    if not status:
        print (err_msg)
    print (err_msg)
            
def create_db_and_schema():
    try:
        conn = sqlite3.connect("hash.db")
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS avhash (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                hash TEXT UNIQUE
            );
        ''')

        conn.commit()
        conn.close()
        print("Database and table created successfully.")
    except Exception as e:
        print(f"Error creating the database,{e}")
    
help = '''
🛡️-SafeBytes
A md5 based malware scanner

Please Chose your action --

1.Create and setup schema only for first time
2.Update hash db
3.Scan a file
'''

def main():
    print (f"{Fore.YELLOW}{help}")
    usr_input = int(input(f"{Fore.BLUE}Plese enter you action : "))
    if usr_input == 1:
        create_db_and_schema()
    elif usr_input == 2:
        update_hash()
    elif usr_input == 3:
        user_file_name = input(f"{Fore.YELLOW}Enter the file name : ")
        if not user_file_name:
            sys.exit(1)
        scan_file(user_file_name)
    else:
        print(f"{Fore.RED}Invalid Selcetion.")


if __name__ == '__main__':
    main()