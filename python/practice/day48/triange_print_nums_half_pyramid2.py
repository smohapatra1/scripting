#Example 4: – Print a number pattern using a for loop and range function - Number Pattern Example 2: Triangular full pyramid number pattern
'''
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
'''
def triag(n):
    for i in range(1,n):
        for j in range(i,0,-1):
            print (j , end=" ")
        print ("\r")

triag(int(input("Enter the number : ")))
