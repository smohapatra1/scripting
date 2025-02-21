#   https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/

with open('file.txt', 'r') as f:
    lines = f.readlines()
    for row in lines:
        word = 'line 4'
        if row.find(word) != -1:
            print ('string exists in the file :' + word)
            print ('Line Number :', lines.index(row))