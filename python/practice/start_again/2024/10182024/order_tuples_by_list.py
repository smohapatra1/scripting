#   https://www.geeksforgeeks.org/python-order-tuples-by-list/

def OrderList(test_list, ord_list):
    print ("Current list:  " + str(test_list) + "\n" )
    print ("Things to ordered in ordered list: " + str(ord_list) + "\n")
    temp = dict(test_list)
    res = [(key, temp[key]) for key in ord_list]
    return res

if __name__ == "__main__":
    test_list = [('Gfg', 3), ('best', 9), ('CS', 10), ('Geeks', 2)]
    ord_list = ['Geeks', 'best', 'CS', 'Gfg']
    print ("Results after ordering the list : ", OrderList(test_list, ord_list))