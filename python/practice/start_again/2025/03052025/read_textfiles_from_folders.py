#   https://www.geeksforgeeks.org/how-to-read-multiple-text-files-from-folder-in-python/

import os 

path = "03052025"
os.chdir(path)
def read_files(file_path):
    with open(file_path, 'r') as f:
        print (f.read())
for file in os.listdir():
    if file.endswith('.txt'):
        file_path = f"{path}\{file}"
        read_files(file_path)