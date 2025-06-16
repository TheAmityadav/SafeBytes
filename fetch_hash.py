import requests
DB = 'hash.db'
import sqlite3


def fetch_hash_from_virush_share():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    url_count = 0
    while True:
        url = (f"https://hashes.virusshare.net/VirusShare_{url_count:05}.md5")
        try: 
            response = requests.get(url,stream=True, timeout=10)
            response.raise_for_status()
            new_hashes = []
            if response.status_code != 200:
                break
            for hash in response.iter_lines(decode_unicode=True):
                hash = hash.strip().lower()
                if len(hash) == 32 and all(c in '0123456789abcdef' for c in hash):
                    new_hashes.append((hash,))
            cursor.executemany("INSERT OR IGNORE INTO avhash (hash) VALUES (?)",new_hashes)
            conn.commit()
            url_count+=1
        except Exception as e:
            print(f"Error feting the hashes",{e})
            break
    cursor.close()
    conn.close()



