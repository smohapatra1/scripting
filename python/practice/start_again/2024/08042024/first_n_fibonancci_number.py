#   Write a Program To Print the First N Fibonacci Numbers.


def Fibonancci(n):
    i = []
    a = 1 
    b = 1 
    x = 1 
    for x in range(n):
        i.append(a)
        a = b 
        b = a + b 
    print (i)


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    result = Fibonancci(n)