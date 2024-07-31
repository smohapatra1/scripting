#   String Palindrome

def Palindrome(n):
    if n == n[::-1]:
        print ('Palindrome')
    else:
        print ('Not Palindrome')

if __name__ == "__main__":
    n = input("Enter the string: ")
    result = Palindrome(n)