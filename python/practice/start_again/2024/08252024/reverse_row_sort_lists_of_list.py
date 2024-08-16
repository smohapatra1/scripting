#   https://www.geeksforgeeks.org/python-reverse-row-sort-in-lists-of-list/

def ReverseList(test_list):
    for i in test_list:
        i.sort(reverse=True)
    return test_list

if __name__ == "__main__":
    test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]
    result = ReverseList(test_list)
    print (result)