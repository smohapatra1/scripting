#   https://www.geeksforgeeks.org/python-replace-substrings-from-string-list/

def Replace(test_list1, test_list2):
    print ("Previous String : " + str(test_list1))
    res = [sub.replace(sub2[0], sub2[1]) for sub in test_list1 for sub2 in test_list2 if sub2[0] in sub]
    return res

if __name__ == "__main__":
    test_list1 = ['GeeksforGeeks', 'is', 'Best', 'For', 'Geeks', 'And', 'Computer Science']
    test_list2 = [['Geeks', 'Gks'], ['And', '&'], ['Computer', 'Comp']]
    result = Replace(test_list1, test_list2)
    print (result)