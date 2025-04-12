#   https://www.geeksforgeeks.org/how-to-detect-file-changes-using-python/

import hashlib
import time

def calculate_file_hash(file_path):
    with open(file_path, "rb") as f:
        file_hash = hashlib.sha256(f.read()).hexdigest()
    return file_hash

def detect_file_changes(file_path):
    last_hash = calculate_file_hash(file_path)
    while True:
        current_hash = calculate_file_hash(file_path)
        if current_hash != last_hash:
            print("File has changed!")
            last_hash = current_hash
        time.sleep(1)

# Usage
detect_file_changes("file.txt")