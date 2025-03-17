#   https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/

import shutil

def merge_files(file1, file2, new_file):
    with open(new_file, 'wb') as outfile:
        for filename in [file1, file2]:
            with open(filename, 'rb') as infile:
                shutil.copyfileobj(infile, outfile)
    print(f'{file1} and {file2} merged into {new_file}')

if __name__ == "__main__":
    file1 = 'file.txt'
    file2 = 'file2.txt'
    new_file = 'file3.txt'
    merge_files(file1, file2, new_file)