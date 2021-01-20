#Python Program to Find Largest of Three numbers
#Write a Python program to find largest of three numbers using 
#Elif Statement and Python Nested If. 
#In Python programming, we have many approaches to find largest number among three numbers.
# a > b > c - a is largest
# b > c > a - b is largest 
# c >b > a  - c is largest


def largest(a,b,c):
    if a > b and a > c:
        print ("%d is larger than %d and %d" %(a,b,c))
    elif b > c and c > a:
        print ("%d is larger than %d and %d" %(b,c,a))
    elif c > b and b > a:
        print ("%d is larger than %d and %d" %(c,b,a))
    else:
        print ("%d is equal to %d and %d" %(a,b,c))

def main():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    largest(a,b,c)
    

if __name__ == "__main__":
    main()