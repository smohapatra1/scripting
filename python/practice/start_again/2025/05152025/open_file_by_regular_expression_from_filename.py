#   https://www.geeksforgeeks.org/open-a-file-by-regular-expression-in-python/

import re

def open_by_regex(file_pattern):
    files = ["report.txt", "data.csv", "file.txt"]
    pattern = re.compile(r'(\d{4})(\d{2})(\d{2})_' + file_pattern)
    for file_name in files:
        match = pattern.match(file_name)
        if match:
            year, match , day = match.group()
            print (f"Date: {year}-{match}-{day}, File: {file_name}")

open_by_regex(r'.*\.txt')