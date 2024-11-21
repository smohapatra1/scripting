#   https://www.geeksforgeeks.org/python-program-to-check-whether-the-string-is-symmetrical-or-palindrome/?ref=leftbar-rightbar

def Symmetrical(s):
    l = len(s)
    mid = l // 2
    if l % 2 == 0 :
        return s[:mid] == s[mid:]
    else:
        return s[:mid] == s[mid+1:]

def Palindrome(s):
    if s == s[::-1]:
        return "Palindrome"

if __name__ == "__main__":
    s = 'khokho'
    # s = 'amaama'
    print ("Current String : ", s )
    if Symmetrical(s):
        print ("String is Symmetrical      : ", Symmetrical(s))
    else:
         print ("String is Not Symmetrical : ", Symmetrical(s))
    if Palindrome(s):
        print ("String is Palindrome       : ", Palindrome(s))
    else:
         print ("String is Not Palindrome  : ", Palindrome(s))
    