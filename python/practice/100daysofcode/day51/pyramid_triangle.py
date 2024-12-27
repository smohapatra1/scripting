#Print full Triangle pyramid using stars 
def triag(x):
    for i in range (0, x):
        k = 2*x -2
        for k in range(0,-1):
            print("*", end=" ")
        k = k - 2
        for j in range (0, k):
            print ("*", end =" ")
        print("\r")

triag(int(input("Enter a number ")))
