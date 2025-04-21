#   https://www.geeksforgeeks.org/python-finding-n-character-words-in-a-text-file/

import re

def find_n_char(file_path, n):
    with open(file_path, 'r') as f:
        contents = f.read()
    pattern = r'\b\w{' + str(n) + r'}\b'
    words_with_n_char = re.findall(pattern, contents)
    return words_with_n_char
file_name = 'file.txt'
n = 3 
result = find_n_char(file_name, n)
print (f"Words containing {n} characters : ")
print (result)
