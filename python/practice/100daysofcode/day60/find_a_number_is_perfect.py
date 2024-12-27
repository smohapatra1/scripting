# Find if a number is perfect
#A perfect number is a number whose sum of the all the divisors (excluding itself) is equal to itself. For example: divisors of 6 (excluding 6 are) : 1, 2, 3 and their sum is 1+2+3 = 6. Therefore, 6 is a perfect number. 

def perfect(x):
    sum = 1
    i = 2
    while i * i <= int(x):
        if int(x) % i == 0 :
            sum = sum + i + int(x)/i
            print ("sum : ", sum)
        i +=1
    #return (True if sum == x and x !=1 else False)
    if sum == int(x):
        print (x, "is a perfect number")
    else:
        print (x, "is NOT a perfect number")

perfect(input("Enter a number : "))

