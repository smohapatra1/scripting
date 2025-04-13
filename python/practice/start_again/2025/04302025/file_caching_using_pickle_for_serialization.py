#   https://www.geeksforgeeks.org/how-to-implement-file-caching-in-python/

import pickle

file_cache = {}

def read_pickle_file(file_path):
    if file_path not in file_cache:
        with open(file_path, 'rb') as f:
            f_content = pickle.load(f)
            file_cache[file_path] = f_content
    return file_cache[file_path]

data = {'website': 'wich.com'}
with open('file.txt', 'wb') as f2:
    pickle.dump(data, f2)
result = read_pickle_file('file.txt')
print(result)