#   https://www.geeksforgeeks.org/python-key-with-maximum-unique-values/

def MaxValue(test_dict):
    Max_Value = 0 
    Max_Key = None
    for i in test_dict:
        if len(set(test_dict[i])) > Max_Value:
            Max_Value = len(set(test_dict[i]))
            Max_Key = i
    return Max_Key

if __name__ == "__main__":
    test_dict = {"Gfg": [5, 7, 5, 4, 5],
             "is": [6, 7, 4, 3, 3],
             "Best": [9, 9, 6, 5, 5]}
    print ("Maximum values are : ", MaxValue(test_dict))