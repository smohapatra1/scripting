#   https://www.geeksforgeeks.org/python-substring-presence-in-strings-list/

def Sub(test_list1, test_list2):
    # using loop to iterate
    res = []
    for ele in test_list1 :
        temp = False
    
        # inner loop to check for
        # presence of element in any list
        for sub in test_list2 :
            if ele in sub:
                temp = True
                break   
        res.append(temp)
    return res


if __name__ == "__main__":
    test_list1 = ["Gfg", "is", "Best"]
    test_list2 = ["I love Gfg", "Its Best for Geeks", "Gfg means CS"]
    result = Sub(test_list1, test_list2)
    print (result)