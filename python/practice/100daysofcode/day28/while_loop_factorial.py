#/usr/bin/python
#Write a program using while loop, which asks the user to type a positive integer, n, and then prints the factorial of n. A factorial is defined as the product of all the numbers from 1 to n (1 and n inclusive). For example factorial of 4 is equal to 24. (because 1*2*3*4=24)
a = int(input("Enter a number "))
f = 1
count = 1
while f <= a :
    count = f * count
    f +=1
    #count +=1
    print ("v : % d and c %d " % (f, count))
print (count)
