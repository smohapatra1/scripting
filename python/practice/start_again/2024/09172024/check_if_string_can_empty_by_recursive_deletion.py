#   https://www.geeksforgeeks.org/string-slicing-python-check-string-can-become-empty-recursive-deletion/

def StrRecursive(str1, sub_str1):
    if len(str1) == 0 and len(sub_str1) == 0 :
        return True
    if len(sub_str1) == 0:
        return False
    while (len(str1) != 0) :
        index = str1.find(sub_str1)
        if (index == (-1)):
            return False
        str1 = str1[0:index] + str1[index + len(sub_str1):]
    return True

if __name__ == "__main__":
    # str1 = 'GEEGEEKSKS'
    # sub_str1 = "GEEKS"
    str1 = 'GEEGEEKSKS123'
    sub_str1 = "GEEKS"
    res = StrRecursive(str1, sub_str1)
    print (res)
