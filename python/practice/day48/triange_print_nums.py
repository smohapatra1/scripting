#Example 1: – Print a number pattern using a for loop and range function
def triag(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print (i , end=" ")
        print ("\r")

triag(int(input("Enter the number : ")))
