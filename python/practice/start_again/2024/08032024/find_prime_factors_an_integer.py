#   Write a Program To Find the Prime Factors of an Integer.

def PrimeFactor(n):
    i = 2 
    while i * i < n :
        while n % i == 0:
            n = n/i
        i = i+1
    print (n)
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    result = PrimeFactor(n)