#Write a program that asks the user for a positive number 'n' as input. Assume that the user enters a number greater than or equal to 3 and print a triangle as described below. For example if the user enters 6 then the output should be:

def triang(x):

    if x >= 3 :
        #spaces
        k = 2*x - 2
        for i in range(0,x):
            for j in range(0,k):
                print (end=" ")
            k = k - 2
            for j in range(0,i+1):
                print ("* ", end="")
            print("\r")
    else:
        print ("Enter values > 3")

triang(int(input("Enter a number : ")))
