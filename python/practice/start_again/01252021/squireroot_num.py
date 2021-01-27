#Python Program to find Square root of a Number
#Write a Python Program to find Square root of a Number using sqrt and pow function with an example.
#Using math function 
from math import sqrt
from math import pow
def main():
    a = int(input("Enter the number: "))
    print ("Built in function: Sqrt of %d is %d" %(a, sqrt(a)))

def square():
    a = int(input("Enter the number : "))
    print ("Built in function pow: Sqrt of %d is %d" %(a, pow(a, 0.5)))

if __name__ == "__main__":
    main()
    square()