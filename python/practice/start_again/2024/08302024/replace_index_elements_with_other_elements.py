#   https://www.geeksforgeeks.org/python-replace-index-elements-with-elements-in-other-list/?ref=leftbar-rightbar
import numpy as np

def replace(test_list1, test_list2):
    # Solution - 1 
    # res = [test_list1[idx] for idx in test_list2]
    # Solution - 2 
    res = np.take(test_list1, test_list2)
    return res

if __name__ == "__main__":
    test_list1 = ['Gfg', 'is', 'best']
    test_list2 = [0, 1, 2, 1, 0, 0, 0, 2, 1, 1, 2, 0]
    result = replace(test_list1, test_list2)
    print (result)
