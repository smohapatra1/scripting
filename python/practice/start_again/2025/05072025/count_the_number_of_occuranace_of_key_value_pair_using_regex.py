#   https://www.geeksforgeeks.org/python-program-to-count-the-number-of-occurrences-of-a-key-value-pair-in-a-text-file/

import re
def count_key_value_pairs(file_path, key, value):
    with open(file_path, 'r') as f:
        data = f.read()
    pattern = r'\b{}=={}\b'.format(re.escape(key), re.escape(value))
    occurrences = len(re.findall(pattern, data))
    return occurrences
if __name__ == "__main__":
    file_path = 'file.txt'
    key_to_find = 'i'
    value_to_find = 'g'
    occurrences = count_key_value_pairs(file_path, key_to_find, value_to_find)
    print (f"Number of occurrences of '{key_to_find}={value_to_find}': {occurrences}")