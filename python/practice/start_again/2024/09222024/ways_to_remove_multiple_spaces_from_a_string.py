#   https://www.geeksforgeeks.org/python-ways-to-remove-multiple-empty-spaces-from-string-list/?ref=leftbar-rightbar

def Remove(test_list):
    res = []
    for ele in test_list:
        if ele.strip():
            res.append(ele)
    return res

if __name__ == "__main__":
    test_list = ['gfg', ' ', ' ', 'is', '         ', 'best']
    result = Remove(test_list)
    print (result)