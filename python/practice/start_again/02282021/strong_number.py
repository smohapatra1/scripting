#Python Program to find Strong Number
#Write a Python Program to find Strong Number using While Loop, For Loop, and factorial function with an example.
def main():
    n = int(input("Enter a number: "))  
    temp=n
    sum = 0 
    while temp > 0:
        fact = 1
        i = 1
        reminder = temp % 10 
        while i <=reminder:
            fact = fact * i  
            i = i + 1
        print ("factorial of %d = %d " % ( reminder, fact))
        sum = sum + fact
        temp = temp // 10
    print ("Sum of given number %d = %d " %(n, sum)) 
    if sum == n :
        print ("%d is a strong number" % n)
    else:
        print ("%d is not a strong number" % n)

if __name__ == "__main__":
    main()