#   https://www.geeksforgeeks.org/python-count-strings-with-substring-string-list/?ref=leftbar-rightbar

# Brute force 
# Other way using find

def CountString(test_list, subs):
    # Solution - 01 
    # res = len([i for i in test_list if subs in i])
    # return res

    # Solution - 02
    res = 0  
    for i in test_list:
        if i.find(subs) != -1:
            res +=1
    return res



if __name__ == "__main__":
    test_list = ['GeeksforGeeks', 'Geeky', 'Computers', 'Algorithms', 'GeekOOO']
    subs = 'Geek'
    result = CountString(test_list, subs)
    print (result)