#   https://www.geeksforgeeks.org/python-program-to-count-the-number-of-occurrences-of-a-key-value-pair-in-a-text-file/

from collections import Counter
def count_key_value_pairs(file_path, key, value):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    count = 0 
    for line in lines:
        line_key, line_value = line.strip().split('=')
        if line_key == key and line_value == value:
            count += 1
    return count

if __name__ == "__main__":
    file_path = 'file.txt'
    key_to_find = 'am'
    value_to_find = 'good'
    occurrences = count_key_value_pairs(file_path, key_to_find, value_to_find)
    print ("Number of occurrences '{key_to_fine}={value_to_find}': {occurrences}") 