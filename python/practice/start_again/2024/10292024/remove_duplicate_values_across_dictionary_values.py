#   https://www.geeksforgeeks.org/python-remove-duplicate-values-across-dictionary-values/
from collections import Counter

def RemDup(test_dict):
    cnt = Counter()
    for idx in test_dict.values():
        cnt.update(idx)
    res = {idx: [key for key in j if cnt[key] == 1] for idx, j in test_dict.items()}
    return res


if __name__ == "__main__":
    test_dict = {'Manjeet': [1, 4, 5, 6],
             'Akash': [1, 8, 9],
             'Nikhil': [10, 22, 4],
             'Akshat': [5, 11, 22]}
    print ("Values after removing duplicate values : ", RemDup(test_dict))