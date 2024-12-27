#print triangle
def triag(x):
    for i in range(1,x):
        for j in range(i,0,-1):
            print (j, end=" ")
        print ("\r")
triag(int(input("Enter a number : ")))
