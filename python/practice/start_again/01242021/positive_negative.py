#Python Program to check Number is Positive or Negative
#Write a Python Program to check Number is Positive or Negative with a practical example.

def main():
    a = int(input("Enter a number: "))
    if a > 0 :
        print ("{} is positive".format(a)) 
    elif a < 0 :
        print ("{} is negative".format(a))
    else:
        print ("{} is zero".format(a))
if __name__ == "__main__":
    main()