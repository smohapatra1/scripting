#   https://www.geeksforgeeks.org/python-test-if-string-is-subset-of-another/

#   Use Set
#   Use the inbuilt function - issubset


def Subset(str1, substr):
    res = set(substr).issubset(str1)
    return res

if __name__ == "__main__":
    str1 = 'geeksforgeeks'
    substr = 'gfks'
    result = Subset(str1, substr)
    print (result)