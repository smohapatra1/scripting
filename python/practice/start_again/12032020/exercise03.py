#Problem 3
#Write a function that asks for an integer and prints the square of it. 
#Use a while loop with a try, except, else block to account for incorrect inputs.
def square():
    while True:
        try:
            x = int(input("Enter a number : "))
        except:
            print ("Enter an integer")
            continue
        else:
            y = x ** 2
            print ("Square of {} is {}".format(x,y))
            break
if __name__ == "__main__":
    square()