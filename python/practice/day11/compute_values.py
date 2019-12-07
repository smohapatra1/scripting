#!/usr/bin/python
#Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
x=int(raw_input("Enter a number : "))
n1 = int("%s " %x)
n2 = int("%s%s" % (x,x))
n3 = int("%s%s%s" %(x,x,x))

print (n1+n2+n3)
