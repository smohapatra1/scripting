#sum of odd numbers from a list
import os
def odd(x):
    y = x.split()
    print ("Numbers are : y")
    sum = 0 
    for i in y :
        if int(i) % 2 == 1:
            sum += int(i)
    print ("Total Sum ", sum)
odd(input("Enter numbers by spaces : "))
