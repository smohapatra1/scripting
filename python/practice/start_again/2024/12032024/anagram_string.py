#   https://www.geeksforgeeks.org/problems/anagram-1587115620/1

from collections import Counter

def Anagram(s1, s2):
    return sorted(set(s1)) == sorted(set(s2))
    # return Counter(s1) == Counter(s2)
    # return set(s1) == set(s2) and len(s1) == len(s2)


if __name__ == "__main__":
    s1 = 'listen'
    s2 = 'silent'
    print (Anagram(s1, s2))
