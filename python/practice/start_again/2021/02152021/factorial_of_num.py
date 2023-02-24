#Python Program to find Factorial of a Number
#Write a Python program to Find Factorial of a Number using For Loop, While Loop, Functions, and Recursion. 
# The Python Factorial denoted with the symbol (!). The Factorial of number is the product of all numbers less than or equal to that number & greater than 0.

def main():
    n = int(input("Enter a number: "))
    fact = 1 

#Loop
    for i in range (1, n+1):
        fact = fact * i     
    print ("The factorial of %d is %d" % ( n, fact))
if __name__ == "__main__":
    main()