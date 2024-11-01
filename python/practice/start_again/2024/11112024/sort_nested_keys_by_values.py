#   https://www.geeksforgeeks.org/python-sort-nested-keys-by-value/

def Sorted(test_dict):
    res = {key : dict(sorted(val.items(), key = lambda ele:ele[1])) for key, val in test_dict.items()}
    return res

if __name__ == "__main__":
    test_dict = {'Nikhil' : {'English' : 5, 'Maths' :  2, 'Science' : 14},
             'Akash' : {'English' : 15, 'Maths' :  7, 'Science' : 2},
             'Akshat' : {'English' : 5, 'Maths' :  50, 'Science' : 20}}
    print ("Results after sorting : ", Sorted(test_dict))