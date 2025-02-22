#   https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/

with open ('file.txt', 'r') as f:
    for index, line in enumerate(f):
        if 'line 2' in line:
            print ("String exists in the file")
            break
    print ('string doesn\'t exist ')