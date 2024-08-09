#    Calculate the factorial of a given number.

def Factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * Factorial(n-1)

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = Factorial(n)
    print (result)