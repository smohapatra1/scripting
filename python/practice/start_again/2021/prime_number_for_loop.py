# Prime number using for loop

def main():
    n = int(input("Enter the number: "))
    #a = []
    count = 0 
    for i in range(2, n//2+1):
        if n % i == 0:
            count = count +1
            break
    if count ==0 and n !=1:
        print ("%d is a prime number" % n)
    else:
        print ("%d is NOT a prime number" % n)

if __name__ == "__main__":
    main()