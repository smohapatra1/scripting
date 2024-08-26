#   https://www.geeksforgeeks.org/python-convert-character-matrix-to-single-string/

#   Use Chain 
#   OR use the join 

from itertools import chain

def Matrix(test_list):
    # Solution - 01 
    # res = ''.join(ele for sub in test_list for ele in sub)
    # return res
    
    # Solution - 02 
    res = ''.join(chain(*test_list))
    return res
        

if __name__ == "__main__":
    test_list = [['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'], ['G', 'O', 'O', 'D']]
    result = Matrix(test_list)
    print (result)  