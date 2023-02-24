#Next Prime Number - Have the program find prime numbers 
#until the user chooses to stop asking for the next one.
# Incomplete 
def calculate(a):
    for i in range (2, a+1):
        if a % i == 0 :
            isPrime = 1
            for j in range(2, i//2 +1):
                if i % j == 0:
                    isPrime = 0 
                    break
            if isPrime == 1:
                print ("%d and %d" %(i,a))
def main():
    a = input('Enter the number or \'s\': ')
    current = 1
    while a.lower().startswith('y'):
        current += 1
        while calculate(current) == 0:
            current +=1
        print ("Next Prime is " + str(current))
        a = input("Continue, enter (y/n) ")

if __name__ == '__main__':
    main()
