#Triangle Pyramid
def triangle(x):
    for i in range (0,x):
        for j in range (0,i+1):
            print ("*", end="")
        print ("\r")
triangle(int(input("Enter a value :")))
