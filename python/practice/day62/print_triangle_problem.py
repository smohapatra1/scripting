#Write a program that asks the user for a positive number 'n' as input. Assume that the user enters a number greater than or equal to 3 and print a triangle as described below. For example if the user enters 6 then the output should be:
'''
*
**
***
****
*****
******
*****
****
***
**
*
'''
def triag(x):
    for i in range(0, x):
        for j in range(0, i+1):
            print("*", end="")
        print ("\r")
    for i in range(x,0, -1):
        for j in range(0, i-1):
            print("*", end="")
        print ("\r")

triag(int(input("Enter the number for triag : ")))
