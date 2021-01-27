#Python Program to find Power of a Number
#Write a Python Program to find Power of a Number For Loop, While Loop, and pow function with an example.
from math import pow
def main():
    a = int(input("Enter a number : "))
    print (pow(a, 2 ))
    print ("Power of %d is %d" %(a, a** 2))
if __name__ == "__main__":
    main()