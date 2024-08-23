#   https://www.geeksforgeeks.org/python-prefix-frequency-in-string-list/?ref=leftbar-rightbar

# Use loop
# Use startswith inbuild 

def frequency(test_list, test_sub):
    # Solution - 01 
    # res = sum(sub.startswith(test_sub) for sub in test_list)
    # Solution - 02
    res = 0 
    for i in test_list:
        if i.startswith(test_sub):
            res = res +1 
    return res

if __name__ == "__main__":
    test_list = ['gfgisbest', 'geeks', 'gfgfreak', 'gfgCS', 'Gcourses', 'gfgCaaaaaaS']
    test_sub = 'gfg'
    result = frequency(test_list, test_sub)
    print (result)