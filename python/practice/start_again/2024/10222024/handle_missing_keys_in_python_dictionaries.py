#   https://www.geeksforgeeks.org/handling-missing-keys-python-dictionaries/

def MissingKeys(d):
    if "q" in d:
        print (d['d'])
    else:
        print ("Keys not found")


if __name__ == "__main__":
    # d = { 'a' : 1 , 'b' : 2 }
    d = {'a': 5, 'c': 8, 'e': 2}
    result = MissingKeys(d)