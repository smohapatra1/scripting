'''
print
*
* *
* * *
* * * *
* * *
* *
*
'''
def triag(x):
    for i in range(0,x):
        for j in range(0, i+1):
            print("*", end=" ")
        print("\r")
    for i in range(x,1, -1):
        for j in range(0, i -1):
            print("*", end=" ")
        print("\r")

triag(int(input("Enter the row :")))
