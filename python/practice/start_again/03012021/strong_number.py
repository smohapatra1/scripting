#Find the strong number 

def main():
    n = int(input("Enter a number: "))    
    temp = n  
    sum = 0 
    while temp > 0 :
        fact = 1
        i = 1
        reminder = temp % 10 
        while i <= reminder:
            fact = fact * i 
            i = i +1
        print ( "Fact is %d and Sum is %d" % ( reminder,fact))
        sum = sum + fact
        temp = temp // 10
    print ("Sum of given number %d = %d" %( n, sum))   
    if sum == n:
        print ("%d is a Strong Number" %n)
    else:
        print("%d is Not a strong Number" % n ) 

if __name__ == "__main__":
    main()