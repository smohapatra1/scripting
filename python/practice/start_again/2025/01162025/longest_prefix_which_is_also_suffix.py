#   https://www.geeksforgeeks.org/longest-prefix-also-suffix/

def LongestPrefix(s):
    res = 0 
    n = len(s)
    for length in range(1, n ):
        j = n - length
        flag = True
        for k in range(length):
            if s[k] != s[j+k]:
                flag = False
                break
        if flag:
            res = length
    return res

if __name__ == "__main__":
    s = 'ababab'
    s1 = 'aaaaaa'
    s2 = 'aaa'
    print (LongestPrefix(s))
    print (LongestPrefix(s1))
    print (LongestPrefix(s2))