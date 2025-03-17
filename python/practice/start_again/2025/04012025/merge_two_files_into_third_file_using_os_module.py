#   https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/

import os

def Merge_Files(file1, file2, new_file):
    with open(new_file, 'wb') as outfile:
        for filename in [file1, file2]:
            with open(filename, 'rb') as infile:
                for line in infile:
                    outfile.write(line)
    print(f'{file1} and {file2} merged into {new_file}')
if __name__ == "__main__":
    file1 = 'file.txt'
    file2 = 'file2.txt'
    new_file = 'file3.txt'
    Merge_Files(file1, file2, new_file)