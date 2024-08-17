#   https://www.geeksforgeeks.org/python-pair-elements-with-rear-element-in-matrix-row/

def PairList(test_list):
    print ("Previous elements " + str(test_list))
    res = []
    for i in test_list:
        res.append([[ele, i[-1]] for ele in i[:-1]])
    print ("Post elements " + str(res))

if __name__ == "__main__":
    test_list = [[4, 5, 6], [2, 4, 5], [6, 7, 5], [9, 10, 11]]
    result = PairList(test_list)