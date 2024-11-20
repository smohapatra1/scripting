#   https://www.geeksforgeeks.org/problems/palindrome-string0817/1

def Palindrome(s):
    return s == s[::-1]

if __name__ == "__main__":
    # s = "abba"
    s = 'madam'
    print (Palindrome(s) )