#   https://www.geeksforgeeks.org/python-group-sublists-by-another-list/

def groups(test_list1, test_list2):
    temp = []
    for i in test_list1:
        if i in test_list2:
            if temp:
                yield temp
                temp = []
            yield i
        else:
            temp.append(i)
    if temp:
        yield temp

if __name__ == "__main__":
    test_list1 = [8, 5, 9, 11, 3, 7]
    test_list2 = [9, 11]
    res = list(groups(test_list1, test_list2))
    print (res)