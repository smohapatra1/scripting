#   https://www.geeksforgeeks.org/wildcard-pattern-matching/

def wildCardMatch(txt, pat, n , m ):
    if m == 0 :
        return n == 0 
    if n == 0 :
        for i in range(m):
            if pat[i] != '*':
                return False
            return True
    if txt[n-1] == pat[m-1] or pat[m-1] == '?':
        return wildCardMatch(txt, pat, n-1, m-1)
    if pat[m-1] == '*':
        return wildCardMatch(txt, pat, n, m-1) or wildCardMatch(txt, pat, n-1, m )
    return False

if __name__ == "__main__":
    txt = "abcde"
    pat = "a*de"
    n = len(txt)
    m = len(pat)
    txt1 = 'baaabab'
    pat1 = 'a*ab'
    a = len(txt)
    b = len(pat)

    print("True" if wildCardMatch(txt, pat, n, m ) else "False")
    print("True" if wildCardMatch(txt1, pat1, a, b ) else "False")