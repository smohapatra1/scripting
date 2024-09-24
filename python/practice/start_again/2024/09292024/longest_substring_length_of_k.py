#   https://www.geeksforgeeks.org/python-longest-substring-length-of-k/

def Longest(test_str, K ):
    cnt = 0
    res = 0
    for idx in range(len(test_str)):
        # increment counter on checking
        if test_str[idx] == K:
            cnt += 1
        else:
            cnt = 0 
        # retaining max
        res = max(res, cnt)
    return res

if __name__ == "__main__":
    test_str = 'abcaaaacbbaa'
    K = 'a'
    result = Longest(test_str, K )
    print (result)