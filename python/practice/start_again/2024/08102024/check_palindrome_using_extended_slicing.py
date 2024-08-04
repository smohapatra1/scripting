#   Checking for Palindrome Using Extended Slicing Technique

def Palindrome(str1, str2):
    str1 = list(str1.upper())
    str2 = list(str2.upper())
    if str1 == str2[::-1]:
        return 'True'
    else:
        return 'False'

if __name__ == "__main__":
    str1 = 'Kayak'
    str2 = 'Kayak'
    result = Palindrome(str1, str2)
    print (result)