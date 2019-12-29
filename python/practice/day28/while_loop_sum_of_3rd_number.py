#!/usr/bin/python
#Write a program using while loop, which prints the sum of every third numbers from 1 to 1001 ( both 1 and 1001 are included)
num = 1
count = 0 
while num < 1001:
    print ("num : % d " % num)
    count = count + num
    num = num + 3
print (count)
