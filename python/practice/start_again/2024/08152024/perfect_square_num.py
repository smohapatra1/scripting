#   Check if a given number is a perfect square.

def perfect_square(n):
    if (n**0.5)**2 == n:
        return 'A perfect square'
    else:
        return 'NOT A perfect square'

if __name__ == "__main__":
    n = int(input("Enter a number:  "))
    result = perfect_square(n)
    print (result)