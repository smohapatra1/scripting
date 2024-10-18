#   https://www.geeksforgeeks.org/python-group-similar-items-to-dictionary-values-list/

from collections import defaultdict

def GroupList(test_list):
    res = defaultdict(list)
    for ele in test_list:
        res[ele].append(ele)
    return res

if __name__ == "__main__":
    test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
    print ("Results after grouping similar items ", str(GroupList(test_list)))