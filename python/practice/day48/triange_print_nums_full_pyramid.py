#Example 3: – Print a number pattern using a for loop and range function - Number Pattern Example 2: Triangular half pyramid number pattern
'''
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
1 2 3 4 5 6 7
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8 9
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
'''
def triag(n):
    for i in range(1,n):
        for j in range(1,i+1):
            print (j , end=" ")
        print ("\r")
    for i in range(n,1,-1):
        for j in range(1,i-1):
            print (j , end=" ")
        print ("\r")

triag(int(input("Enter the number : ")))
