#   https://www.geeksforgeeks.org/python-find-duplicate-characters-string/

from collections import Counter

def DupChar(s):
    wc = Counter(s)
    print ("Chars are : ", + wc)
    for letter, count in wc.items():
        if count > 1 :
            print ("Duplicate chars are :" + str(letter))

if __name__ == "__main__":
    s = 'geeksforgeeks'
    res = DupChar(s)