#   https://www.geeksforgeeks.org/python-find-duplicate-characters-string/

from collections import Counter
def FindDupe(s):
    WC = Counter(s)
    for letter, count in WC.items():
        if count > 1:
            print (letter)


if __name__ == "__main__":
    # s = 'hello'
    s = 'geeksforgeeks'
    result = FindDupe(s)