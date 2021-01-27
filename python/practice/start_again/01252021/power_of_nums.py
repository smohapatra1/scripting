#Python Program to find Power of a Number
#Write a Python Program to find Power of a Number For Loop, While Loop, and pow function with an example.
from math import pow
def main():
    a = int(input("Enter a number: "))
    b = int(input("Enter the exonent value: "))
    print ("{}' exponent of {} is : {}".format(b,a, pow(a,b)))
if __name__ == "__main__":
    main()