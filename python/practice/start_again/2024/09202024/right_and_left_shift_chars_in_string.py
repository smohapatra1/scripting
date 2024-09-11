#   https://www.geeksforgeeks.org/python-right-and-left-shift-characters-in-string/?ref=leftbar-rightbar

def Rotate(test_str, r_rot, l_rot):
    temp = (r_rot - l_rot) % len(test_str)
    res = test_str[temp:] + test_str[: temp]
    return res

if __name__ == "__main__":
    test_str = 'geeksforgeeks'
    r_rot = 7
    l_rot = 3 
    result = Rotate(test_str, r_rot, l_rot)
    print (result)