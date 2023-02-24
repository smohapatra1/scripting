#Given an integer N. 
#The task is to find the next prime number 
#i.e. the smallest prime number greater than N.
import math

def nextPrime(a):
    prime = True
    np = a + 1
    while True:
        for i in range (2, np):
            if np % i == 0 :
                prime = True
                break
            if prime:
                print (np)
                #If you want you can break 
                return (np)
            else:
                np = np + 1 
                if np % 2 == 0 :
                    np = np + 1
                prime = True 
def main():
    a = int(input("Enter a number : "))
    if a > 2:
        nextPrime(a)

if __name__ == '__main__':
    main()