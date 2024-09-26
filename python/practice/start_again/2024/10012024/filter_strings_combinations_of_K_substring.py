#   https://www.geeksforgeeks.org/python-filter-strings-combination-of-k-substrings/

from itertools import permutations

def Combinations(test_list, substr_list, K ):
    perms = list(set(map(''.join, permutations(substr_list, r = K ))))
    res = []
    for i in perms:
        if i in test_list:
            res.append(i)
    return res



if __name__ == "__main__":
    test_list = ["geeks4u", "allbest", "abcdef"]
    substr_list = ["s4u", "est", "al", "ge", "ek", "def", "lb"]
    K = 3
    result = Combinations(test_list, substr_list, K )
    print (result)