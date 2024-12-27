#/usr/bin/python
#Write a function that a accepts a positive number 'r' as the radius of a circle and calculates and returns the area of the circle. Use the value of pi as 3.14
def area(n):
    a =  3.14 * n * n
    print (a)
area(float(input("Enter the radius : ")))
