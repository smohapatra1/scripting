#Given an integer N. The task is to find the next prime number 
#i.e. the smallest prime number greater than N.

def isPrime(a):
    for i in range (2,a+1):
        if a % i == 0:
            prime = 1
            for j in range (2, i // 2 +1  ):
                if i % j == 0:
                    prime = 0 
                    break
            if prime == 1 :
                print ("%d is prime number for %d" % (i, a))

def main():
    a = int(input("Enter a number: "))
    isPrime(a)

if __name__ == '__main__':
    main()