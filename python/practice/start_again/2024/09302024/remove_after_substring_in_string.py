#   https://www.geeksforgeeks.org/python-remove-after-substring-in-string/
import re 
def Remove(test_str, sub_str):
    res = test_str[:test_str.index(sub_str) + len(sub_str)]
    return res

if __name__ == "__main__":
    test_str = 'geeksforgeeks is best for geeks'
    sub_str = 'best'
    result = Remove(test_str, sub_str)
    print (result)