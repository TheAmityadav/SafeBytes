# SafeBytes
SafeBytes - A hash-based antivirus scanner using Python and SQLite

# 🛡️ SafeBytes

**SafeBytes** is a lightweight hash-based antivirus scanner written in Python. It checks local files against a database of known malware hashes using SQLite. This project is intended for educational purposes and demonstrates how malware detection can be performed using file hashing and database lookups.

---

## 🚀 Features

- 🔍 Scans any file or directory recursively
- 🧠 Detects malware using known MD5 hash signatures
- 🗃️ Stores malware hashes in a local SQLite database
- 🌐 Fetches and updates hash lists from public sources (e.g., VirusShare)
- ⚡ Fast performance with optimized hashing and batch DB inserts
- 🧪 Includes test files like [EICAR test file](https://www.eicar.org/?page_id=3950)

---

## 🛠️ Tech Stack

- **Python 3**
- **SQLite3** for local malware database
- **Hashlib** for MD5/SHA256 hash generation
- **Requests** for downloading malware hash lists
- **CLI-based Interface**

---

## 📁 Project Structure
fetch_hash.py - Have the code of fetching
scanner.py - have the code of scanning
main.py - Main code for temrinal CLI
---

NOTE:
Please use option 1 foe first time setup




