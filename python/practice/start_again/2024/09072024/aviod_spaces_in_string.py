#   https://www.geeksforgeeks.org/python-avoid-spaces-in-string-length/

def AvoidSpace(s):
    # Solution - 1 
    # res1 = sum(map(len, s.split()))
    # return res1
    
    # Solution - 2 
    w = s.replace(' ', '')
    return len(w)


if __name__ == "__main__":
    # s = "I am good"
    s = 'geeksforgeeks 33 is   best'
    res = AvoidSpace(s)
    print (res)