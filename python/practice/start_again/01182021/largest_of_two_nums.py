#Python Program to find Largest of Two Numbers
#Write a Python program to find the largest of Two Numbers 
#using Elif Statement and Nested If statement with an example.

def largest(a,b):
    if a > b:
        print ("%d is larger than %d" % (a,b))
    elif ( b > a):
        print ("%d is larger than %d" % (b,a))
    else:
        print ("Both %d and %d are equal" % (a,b))

def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    largest(a,b)

if __name__ == "__main__":
    main()