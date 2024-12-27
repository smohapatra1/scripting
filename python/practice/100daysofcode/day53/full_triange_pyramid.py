#Example 1: Program to print Full Triangle Pyramid pattern using an asterisk (star)
def triag(x):
    if x <=50 :
        #Num of rows
        k = 2* x - 2
        for i in range(1, x):
            for j in range(1,k):
                print(end=" ")
            k = k  - 1
            for j in range(1,i+1):
                print ("*", end=" ")
            print("\r")
    else:
        print("Enter a small number")

triag(int(input("Enter a number : ")))
