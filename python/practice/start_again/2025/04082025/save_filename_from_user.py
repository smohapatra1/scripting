#   https://www.geeksforgeeks.org/how-to-save-file-with-file-name-from-user-using-python/

dir = 'test'
filepath = dir + input("Enter filename:")
with open(filepath, 'w+') as fp:
    pass