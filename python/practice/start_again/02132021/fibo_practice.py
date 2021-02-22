# Fibonanci Series - fibo

def main():
    n = int(input("Enter the numbers you want in series "))
    a = 1
    b = 1 
    i = []
    for x in range(n):
        i.append(a)
        a,b = b, a+b
    print (i)

if __name__ == "__main__":
    main()