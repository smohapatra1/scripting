#Python Program to check if a Number is Odd or Even

def main():
    a = int(input("Enter a number : "))
    if a % 2 == 0 :
        print ("{} is even".format(a))
    else:
        print ("{} is odd".format(a))
if __name__ == "__main__":
    main()