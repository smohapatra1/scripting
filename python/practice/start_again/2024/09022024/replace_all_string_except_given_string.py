#   https://www.geeksforgeeks.org/python-program-to-replace-all-characters-of-a-list-except-the-given-character/

#   Loop through each list 
#   Return replace char if there is no match else replace new char in the loop

def ReplaceChar(test_list, replace_char, rst_char):
    res = [ ele if ele == rst_char else replace_char for ele in test_list ]
    return res

if __name__ == "__main__":
    test_list = ['G', 'F', 'G', 'I', 'S', 'B', 'E', 'S', 'T']
    replace_char = '$'
    rst_char = 'G'
    result = ReplaceChar(test_list, replace_char, rst_char)
    print (result)