#   https://www.geeksforgeeks.org/python-replace-string-by-kth-dictionary-value/?ref=leftbar-rightbar

def Replace(test_list, subs_dict, k ):
    res = [ele if ele not in subs_dict else subs_dict[ele][k] for ele in test_list]
    return res
if __name__ == "__main__":
    test_list = ["Gfg", "is", "Best"]
    subs_dict = {
    "Gfg" : [5, 6, 7], 
    "is" : [7, 4, 2], 
    }
    k = 2
    print ("After replacing the kth value : ", Replace(test_list, subs_dict, k ))