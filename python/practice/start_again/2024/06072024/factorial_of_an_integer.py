#   How do you find the factorial of an integer?

def Factorial(n):
    if n  == 1:
        return n 
    else:
        return (n * Factorial(n-1))

if __name__ == "__main__":
    n = int(input())
    result = Factorial(n)
    print (result)