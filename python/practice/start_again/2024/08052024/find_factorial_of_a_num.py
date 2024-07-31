#   Write a Python program to find the factorial of a number.

def Factorial(n):
    if n == 0:
        return 1
    else:
        return n * Factorial(n-1)

if __name__ == "__main__":
    n = int(input("Enter the number: "))
    result = Factorial(n)
    print (result)