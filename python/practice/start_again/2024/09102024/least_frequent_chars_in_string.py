#   https://www.geeksforgeeks.org/python-least-frequent-character-in-string/?ref=leftbar-rightbar

from collections import Counter

def Least(test_str):
    res = Counter(test_str)
    return min(res, key=res.get)

if __name__ == "__main__":
    test_str = "GeeksforGeeks"
    result = Least(test_str)
    print (result)