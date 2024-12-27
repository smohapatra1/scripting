#!/usr/bin/python
#Write a program which asks the user to type an integer and then prints "Yes" if that integer is divisible by 3, otherwise prints "No"
a = int(raw_input("Enter an integer : "))
b = float( a % 3)
if a % 3 == 0 :
    print ('Yes')
else:
    print ('No')
