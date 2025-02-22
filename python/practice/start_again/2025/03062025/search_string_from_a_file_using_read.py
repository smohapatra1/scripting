#   https://www.geeksforgeeks.org/python-how-to-search-for-a-string-in-text-files/


with open(r'file.txt', 'r') as f:
    content = f.read()
    if "line 4" in content:
        print ("String exists in the file")
    else:
        print("String does not exist in the file")