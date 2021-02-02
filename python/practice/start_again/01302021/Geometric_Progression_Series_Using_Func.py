#G.P series 

def gpcal(a,n,r):
    total = 0 
    value = a 
    print ("G.P Series: ", end=' ')
    for i in range(n):
        print ("%d" %value, end=' ')
        total = total + value 
        value = value * r
    print ("\nSum of G.P series: ", total)

def main():
    a = int(input("Enter the first number: "))
    n = int(input("Enter the numbers you want : "))
    r = int(input("Enter the common ratio: "))
    gpcal(a,n,r)

if __name__ == "__main__":
    main()