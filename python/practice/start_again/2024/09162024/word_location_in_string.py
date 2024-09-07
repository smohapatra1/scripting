#   https://www.geeksforgeeks.org/python-word-location-in-string/

def Find(test_str, word):
    x = test_str.split()
    res = x.index(word)+1
    return res 

if __name__ == "__main__":
    test_str = 'geeksforgeeks is best for geeks'
    word = 'geeks'
    result = Find(test_str, word)
    print (result)