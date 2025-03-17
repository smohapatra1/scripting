#   https://www.geeksforgeeks.org/python-program-to-merge-two-files-into-a-third-file/

filenames = ['file.txt', 'file2.txt']
with open('file3.txt', 'w') as file:
    for names in filenames:
        with open(names) as infile:
            file.write(infile.read())
file.close()