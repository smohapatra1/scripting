#   https://www.geeksforgeeks.org/python-row-wise-element-addition-in-tuple-matrix/

def RowAdd(test_list, cus_eles):
    res = [[sub + (cus_eles[idx], ) for sub in val ] for idx, val in enumerate(test_list)]
    return res

if __name__ == "__main__":
    test_list = [[('Gfg', 3), ('is', 3)], [('best', 1)], [('for', 5), ('geeks', 1)]]
    cus_eles = [6, 7, 8]
    result = RowAdd(test_list, cus_eles)
    print (result)