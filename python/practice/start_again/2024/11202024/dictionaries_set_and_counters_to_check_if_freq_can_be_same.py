#   https://www.geeksforgeeks.org/python-dictionary-set-counter-check-frequencies-can-become/
from collections import Counter

def allSame(input):
    dict = Counter(input)
    s = list(set(dict.values()))
    if len(s) > 2 :
        return 'No'
    elif len(s) == 2 and s[1] - s[0] > 1:
        return 'No'
    else:
        return 'Yes'


if __name__ == "__main__":
    input = 'xxxyyzzt'
    print ("Values are: ", allSame(input))