#Python Program For Armstrong Number
#How to Write Python Program For Armstrong Number Using While Loop, For Loop, Functions, and Recursion?. 
# We also show you, Python program to print Armstrong Numbers between 1 to n.
#Python Armstrong Number

#If the given number is equal to the sum of the Nth power of each digit present in that integer, then that number can be an Armstrong Number in Python. For example, 370 is Armstrong Number.
#Number of individual digits in 370 = 3
#370 = 3³ + 7³ + 0³
#= 27 + 343 + 0 = 370

import os

def main():
    n = int(input("Enter a number : "))
    #Get length of the number 
    Count = 0 
    Sum = 0
    temp = n  
    while ( temp > 0 ):
        temp = temp // 10
        Count = Count + 1
    print ("The Number of digits are : %d" %Count)
    temp = n
    print (temp) 
    while temp > 0 :
        rem = temp % 10
        Sum = Sum + (rem ** Count )
        temp //= 10
    print (Sum) 
    if n == Sum:
        print ("%d is a Armstrong Number " % temp)
    else:
        print ("%d is Not a Armstrong Numbr " % temp )

if __name__ == "__main__":
    main()


