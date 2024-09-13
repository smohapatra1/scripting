#   https://www.geeksforgeeks.org/python-remove-punctuation-from-string/?ref=leftbar-rightbar

import string

def RemovePunc(test_str):
    test_str = test_str.translate(str.maketrans('', '', string.punctuation))
    print (test_str)

if __name__ == "__main__":
    test_str = 'Gfg, is best: for ! Geeks ;'
    result = RemovePunc(test_str)