#   Checking for Palindrome Using Extended Slicing Technique

def palindrome(n, m ):
    n = n.lower()
    m = m.lower()
    if n == m[::-1]:
        print (True)
    else:
        print (False)


if __name__ == "__main__":
    n = input().rstrip()
    m = input().rstrip()
    res = palindrome(n,m)