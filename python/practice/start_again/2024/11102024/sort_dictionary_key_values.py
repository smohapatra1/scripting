#   https://www.geeksforgeeks.org/python-sort-dictionary-key-and-values-list/?ref=leftbar-rightbar

def Sort(test_dict):
    res = {key : sorted(test_dict[key]) for key in sorted(test_dict)}
    return res

if __name__ == "__main__":
    test_dict = {'gfg': [7, 6, 3], 
             'is': [2, 10, 3], 
             'best': [19, 4]}
    print ("Results after sorting : ", Sort(test_dict))