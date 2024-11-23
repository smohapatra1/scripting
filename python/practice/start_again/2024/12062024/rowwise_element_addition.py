#   https://www.geeksforgeeks.org/python-row-wise-element-addition-in-tuple-matrix/

def Rowwise(test_list, cus_eles):
    # res = [[sub + (cus_eles[idx], )for sub in val] for idx, val in enumerate(test_list)]
    # return res  
    res = []
    for i, row in enumerate(test_list):
        res.append(list(map(lambda x:x + (cus_eles[i],), row)))
    return res


if __name__ == "__main__":
    test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
    cus_eles = [6, 7, 8]
    print ("Current strings : ", test_list)
    print ("New list ", cus_eles)
    print ("Final list", Rowwise(test_list, cus_eles))