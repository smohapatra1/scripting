#   https://www.geeksforgeeks.org/problems/101-pattern-count1341/1?page=1&category=Pattern%20Searching&sortBy=submissions
#   https://www.geeksforgeeks.org/count-of-occurrences-of-a-101-pattern-in-a-string/

def countPattern(s):
    l = len(s)
    res = False
    count = 0 
    for i in range(l):
        if s[i] == '1' and res:
            if s[i-1] == '0':
                count +=1
        if s[i] == '1' and res == 0:
            res = True
        if s[i] != '0' and s[i] != '1':
            res = False
    return count

if __name__ == "__main__":
    s = "100001abc101"
    S = "1001ab010abc01001"
    print(countPattern(s))
    print(countPattern(S))