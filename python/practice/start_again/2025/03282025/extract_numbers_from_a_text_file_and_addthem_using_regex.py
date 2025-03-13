#   https://www.geeksforgeeks.org/extract-numbers-from-a-text-file-and-add-them-using-python/

import re

def extract_numbers(file):
    with open(file, 'r') as f:
        lines = f.read()
        numbers = re.findall(r'\d+', lines)
        result = sum(map(int, numbers))
        return result

if __name__ == "__main__":
    file = 'file.txt'
    result = extract_numbers(file)
    print (f"Sum of the numbers in {file} is {result}")