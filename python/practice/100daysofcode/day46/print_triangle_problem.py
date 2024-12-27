#Write a program that asks the user for a positive number 'n' as input. Assume that the user enters a number greater than or equal to 3 and print a triangle as described below. For example if the user enters 6 then the output should be:

def triangle(n):
    if n >= 3 :
        for i in range(1,n):
            for j in range( 1, i+1):
                print ("*" , end="")
            print ("\r")
    else:
        print ("Please enter the number > 3")
triangle(int(input("Enter a number :")))
