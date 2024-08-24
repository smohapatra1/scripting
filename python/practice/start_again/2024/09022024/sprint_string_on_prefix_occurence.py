#   https://www.geeksforgeeks.org/python-split-strings-on-prefix-occurrence/

#   Loop through values
#   if string found or starts with 
#   then append the values with a new value
#   Else - Return the current values 

def Occurence(test_list, pref):
    res = []
    for val in test_list:
        if val.startswith(pref):
            res.append([val])
        else:
            res[-1].append(val)
    return res

if __name__ == "__main__":
    test_list = ["geeksforgeeks", "best", "geeks", "and", "geeks", "love", "CS"]
    pref = "geek"
    result = Occurence(test_list, pref)
    print (result)