# Determine a string is palindrome 

def StringPalindrome(s):
    p = s[::-1]
    if s == p:
        return 'YES'
    else:
        return 'NO'

if __name__ == "__main__":
    s = input()
    result = StringPalindrome(s)
    print (result)