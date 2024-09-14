#   https://www.geeksforgeeks.org/python-remove-suffix-from-string-list/

def Remove(test_list):
    suffix = 'x'
    for word in test_list[:]:
        if word.endswith(suffix):
            test_list.remove(word)
    return test_list


if __name__ == "__main__":
    test_list = ['allx', 'lovex', 'gfg', 'xit', 'is', 'bestx']
    result = Remove(test_list)
    print (result)