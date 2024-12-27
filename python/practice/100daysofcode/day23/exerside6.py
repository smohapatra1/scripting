#!/usr/bin/python
#Write a program which asks the user to enter their age in years (Assume that the user always enters an integer) and based on the following conditions, prints the output exactly as in the following format (as highlighted in yellow):
#When age is less than or equal to 0, your program should print
a = int(raw_input("Enter your age :"))
if a <= 0 :
    print ('UNBORN')
elif a >=0 and a <=150 :
    print ('ALIVE')
else:
    print('VAMPIRE')

