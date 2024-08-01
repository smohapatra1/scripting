#   Write a Python program to reverse a string.

def Reverse(n):
    n1 = n[::-1]
    print (n1)

if __name__ == "__main__":
    n = input("Enter a string: ")
    result = Reverse(n)