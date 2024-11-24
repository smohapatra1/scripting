#   https://www.geeksforgeeks.org/handling-missing-keys-python-dictionaries/


d = {'a':5, 'c' : 6, 'e':7}
if 'q' in d :
    print (d["c"])
else:
    print ("Keys not found")    