#   https://www.geeksforgeeks.org/python-append-content-of-one-text-file-to-another/
import fileinput

def append_file(file1, file2):
    with open(file2, 'a') as f:
        with fileinput.input(files=file1) as f1:
            for line in f1:
                f.write(line)

file1 = 'file.txt'
file2 = 'file3.txt'
append_file(file1, file2)
