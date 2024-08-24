#   https://www.geeksforgeeks.org/python-remove-words-containing-list-characters/?ref=leftbar-rightbar

#   Using loop
#   Using "all" in build 
#   Using List comprehension 

def RemoveChar(test_list, char_list):
    res = [ele for ele in test_list if all(char not in ele for char in char_list) ]
    return res

if __name__ == "__main__":
    test_list = ['gfg', 'is', 'best', 'for', 'geeks']
    char_list = ['g', 'o']
    result = RemoveChar(test_list, char_list)
    print (result)