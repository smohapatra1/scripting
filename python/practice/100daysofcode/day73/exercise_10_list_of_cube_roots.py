#List Methods Exercise 10 (List of Cube Roots))

#Write a function that accepts a positive integer k and returns the ascending sorted list of cube root values of all the numbers from 1 to k (including 1 and not including k). [if k is 1, your program should return an empty list]

def cube(x):
    list=[]
    if x > 0:
        for i in range(1, x):
            cube= i ** (1/3)
            list.append(cube)
        print (list)
cube(int(input("Enter a number : ")))
