#Example 2: – Print a number pattern using a for loop and range function - Number Pattern Example 2: Triangular full pyramid number pattern
def triag(n):
    for i in range(1,n):
        for j in range(1,i+1):
            print (j , end=" ")
        print ("\r")

triag(int(input("Enter the number : ")))
