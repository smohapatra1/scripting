# https://www.geeksforgeeks.org/how-to-implement-file-caching-in-python/

import functools

@functools.lru_cache(maxsize=2)
def read_file_with_lru_cache(file_path):
    with open(file_path, 'r') as file:
        file_contents = file.read()
        print(f"Reading from file: {file_path}")
    return file_contents
result1 = read_file_with_lru_cache('file.txt')
result2 = read_file_with_lru_cache('file.txt')

print (result1)
print (result2)
