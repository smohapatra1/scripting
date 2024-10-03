#   https://www.geeksforgeeks.org/python-records-with-value-at-k-index/

def Records(test_list, ele, K ):
    res = []
    for x, y, z in test_list:
        if y == ele:
            res.append((x,y,z))
    return res

if __name__ == "__main__":
    test_list = [(3, 1, 5), (1, 3, 6), (2, 5, 7), (5, 2, 8), (6, 3, 0)]
    ele = 3 
    K = 1 
    result = Records(test_list, ele, K )
    print (result)