#Example 3: Program to print inverted half pyramid using an asterisk (star)
def triag(x):
    for i in range(x,0,-1):
        for j in range(1, i - 1):
            print("*", end=" ")
        print("\r")

triag(int(input("Enter a value : ")))
