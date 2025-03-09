#   https://www.geeksforgeeks.org/python-copy-contents-of-one-file-to-another-file/

with open('file.txt', 'r') as f1, open('file2.txt', 'a') as f2:
    for line in f1:
        f2.write(line)
f2.close()
f1.close()