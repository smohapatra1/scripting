#   https://www.geeksforgeeks.org/how-to-implement-file-caching-in-python/

import shelve

def read_file_with_cache(file_path):
    with shelve.open('file_cache.db') as cache:
        if file_path not in cache:
            with open(file_path, 'r') as f:
                file_content = f.read()
                cache[file_path] = file_content
                print (f"Reading from the cache : {file_path}")
        else:
            print (f"Reading from the cace : {file_path}")
        return cache[file_path]
with open('file.txt', 'w') as file:
    file.write("this is some new line\n")

result1 = read_file_with_cache('file.txt')
result2 = read_file_with_cache('file.txt')
print (result1)
print (result2)

