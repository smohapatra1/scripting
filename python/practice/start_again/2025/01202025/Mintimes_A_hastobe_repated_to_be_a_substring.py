#   https://www.geeksforgeeks.org/problems/minimum-times-a-has-to-be-repeated-such-that-b-is-a-substring-of-it--170631/1?page=1&category=Pattern%20Searching&sortBy=submissions
#   https://origin.geeksforgeeks.org/minimum-number-of-times-a-has-to-be-repeated-such-that-b-is-a-substring-of-it/

def minRepeats(s1, s2):
    n = len(s1)
    m = len(s2)
    for i in range(n):
        res = 1
        F = True
        for j in range(m):
            if s1[i] != s2[j]:
                F = False
                break 
            i += 1 
            if i == n :
                i = 0 
                if j != m - 1:
                    res += 1
        if F :
            return res
    return -1 

if __name__ == "__main__":
    s1 = "abcd"
    s2 = "cdabcdab"
    s3 = 'ab'
    s4 = 'cab'
    print(minRepeats(s1, s2))
    print(minRepeats(s3, s4))