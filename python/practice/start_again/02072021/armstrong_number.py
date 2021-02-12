# Armstrong Number 

def main():
    n = int(input("Enter a number : "))
    sum = 0 
    count = 0 
    temp = n  
    while temp > 0 :
        temp = temp //10
        count = count + 1
    print ("The number of digits are %d " %count )
    temp =n
    while temp > 0:
        rem = temp % 10
        sum = sum + (rem ** count)
        temp //=10
    print (sum)
    if n == sum :
        print("%d is a Armstrong Number" % n)
    else:
        print("%d is NOT a Armstrong Number" % n)
    

if __name__ == "__main__":
    main()