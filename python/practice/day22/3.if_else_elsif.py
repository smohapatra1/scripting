#!/usr/bin/python

#Write a program which asks the user to type a string and then:
#Print "Dog" if the word "dog" exists in the input string.
#Print "Cat" if the word "cat" exists in the input string. (if both "dog" and "cat" exist in the input string, then you should only print "Dog")
#Otherwise prints "None". (Pay attention to capitalization).
a = str(raw_input("Enter the string : "))
if a == "dog" :
    print ('Dog')
elif a == "cat" :
    print ('Cat')
else:
    print ('None')

