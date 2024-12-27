#!/usr/bin/python
# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers
num=raw_input("Enter the commana separated value : ")
list=num.split(",")
tuples=tuple(list)
print ("list %s" % list)
print ('tuples : ', tuples)
