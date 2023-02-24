#Factorial of a number 

def main():
    n = int(input("Enter a number: "))
    fact = 1 
    for i in range (1, n+1 ):
        fact = fact * i 
    print("Factorial of %d is : %d" % (n,fact))

if __name__ == "__main__" :
    main()