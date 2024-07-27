#   How Do You Figure Out if the Provided String Is a Palindrome?

def Palindrome(n):
    n = n.lower()
    if n == n[::-1]:
        print (True)
    else:
        print (False)
if __name__ == "__main__":
    n = input("Enter the string: ")
    result = Palindrome(n)