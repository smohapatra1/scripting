#   https://www.geeksforgeeks.org/python-test-if-list-contains-elements-in-range/

def ContainsElements(test_list, i, j ):
    # Solution -01
    # res = True
    # for ele in test_list:
    #     if ele < i or ele >=j :
    #         res = False
    #         break
    # return res
    
    #Solution - 02
    res = all(ele >=i and ele < j for ele in test_list)
    return res

if __name__ == "__main__":
    test_list = [4, 5, 6, 7, 3, 9 ]
    i = 3
    j = 10 
    result = ContainsElements(test_list, i, j )
    print (result)