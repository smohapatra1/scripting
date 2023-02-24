#Longest substring without repeating 

def ls(string):
    m = {}
    l = 0 
    r = 0
    ans = 0 
    n = len(string)
    while (l <n and r < n):
        el = string[r]
        if (el in m):
            l = max(l, m[el]+1)
        m[el] = r 
        ans = max(ans,r-l+1)
        r +=1
    return ans
string="abcde123abcdbbabcd"
result = ls(string)
print (result)
