#   https://www.geeksforgeeks.org/check-string-substring-another/

def FirstOccurrence(txt, pat):
    n = len(txt)
    m = len(pat)
    for i in range(n - m + 1 ):
        j = 0 
        while j < m and txt[i+j] == pat[j]:
            j +=1
        if j == m :
            return i 
    return -1 

if __name__ == "__main__":
    txt = "GeeksForGeeks"
    pat = "Fr"
    txt1 = "GeeksForGeeks"
    pat1 = "For"
    print (FirstOccurrence(txt, pat))
    print (FirstOccurrence(txt1, pat1))