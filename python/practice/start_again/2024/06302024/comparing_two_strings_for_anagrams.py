# Comparing two strings for anagrams

def anagrams(n, m ):
    n = list(n.lower())
    n.sort()
    m = list(m.lower())
    m.sort()
    if n == m :
        print (True)
    else:
        print (False)

if __name__ == "__main__":
    n = input().rstrip()
    m = input().rstrip()
    res = anagrams(n, m)