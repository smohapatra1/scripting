#   https://www.geeksforgeeks.org/python-convert-lists-of-list-to-dictionary/?ref=leftbar-rightbar

def ListsDict(test_list):
    # # Solution -01 
    # res = dict()
    # for sub in test_list:
    #     res[tuple(sub[:2])] = tuple(sub[2:])
    # return res
    # Solution - 02 
    res = {tuple(sub[:2]) : tuple(sub[:2]) for sub in test_list}
    return res

if __name__ == "__main__":
    test_list = [['a', 'b', 1, 2], ['c', 'd', 3, 4], ['e', 'f', 5, 6]]
    print ("Result after converting lists to list of Dict", ListsDict(test_list))