#   https://www.geeksforgeeks.org/python-multiple-indices-replace-in-string/?ref=leftbar-rightbar

def Multipleindicies(test_list, test_str, repl_char):
    temp = list(test_str)
    for idx in test_list:
        temp[idx] = repl_char
    res = ''.join(temp)
    return res
    

if __name__ == "__main__":
    test_str = 'geeksforgeeks is best'
    test_list = [2, 4, 7, 10] 
    repl_char = '*'
    result = Multipleindicies(test_list, test_str, repl_char)
    print (result)