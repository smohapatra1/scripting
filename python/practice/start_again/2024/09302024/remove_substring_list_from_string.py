#   https://www.geeksforgeeks.org/python-remove-substring-list-from-string/?ref=leftbar-rightbar

def Replace(test_str, sub):
    for text in sub:
        test_str = test_str.replace(' ' + text + ' ', ' ')
    return test_str

if __name__ == "__main__":
    test_str = "gfg is best for all geeks"
    sub = ['best', 'all']
    result = Replace(test_str, sub)
    print (result)
