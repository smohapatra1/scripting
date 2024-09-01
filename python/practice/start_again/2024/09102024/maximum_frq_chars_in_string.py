#   https://www.geeksforgeeks.org/python-maximum-frequency-character-in-string/?ref=leftbar-rightbar

from collections import Counter

def Max(test_str):
    res = Counter(test_str)
    return max(res, key=res.get)

if __name__ == "__main__":
    test_str = "GeeksforGeeks"
    result = Max(test_str)
    print (result)