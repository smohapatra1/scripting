#   https://www.geeksforgeeks.org/python-minimum-number-subsets-distinct-elements-using-counter/

from collections import Counter

def MinSubsets(input):
    s = Counter(input)
    res = max(s.values())
    return res
if __name__ == "__main__":
    input = [1, 2, 3, 3]
    print ("Minimum subsets are : ", MinSubsets(input))