#   https://www.geeksforgeeks.org/python-ways-to-remove-multiple-empty-spaces-from-string-list/?ref=leftbar-rightbar

# Loop through the list 
# Use strip to remove the spaces 

def RemoveSpace(test_list):
    # Solution - 01 
    # res = []
    # for i in test_list:
    #     if i.strip():
    #         res.append(i)
    # return res 
    # Solution - 02 
    res = [ele for ele in test_list if ele.strip() ]
    return res
if __name__ == "__main__":
    test_list = ['gfg', ' ', ' ', 'is', '         ', 'best']
    result = RemoveSpace(test_list)
    print (result)