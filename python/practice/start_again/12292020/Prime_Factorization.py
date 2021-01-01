#Prime Factorization - Have the user enter a number 
#and find all Prime Factors (if there are any) and display them.
import math
# 

def calculate_prime(a):
    for i in range (2, a +1 ):
        if a % i == 0:
            isPrime = 1
            for j in range (2, i // 2 +1 ):
                if i % j ==0:
                    isPrime = 0 
                    break
            if (isPrime == 1):
                print ("%d is prime factor of given number %d" %(i, a))
                
def main():
    c = []
    a = int(input("Enter a number : "))
    calculate_prime(a)
    #for x in range(a):
    #    i.append(a)
    #print (i)

if __name__ == '__main__':
    main()