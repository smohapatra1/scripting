#!/usr/bin/python
#Convert seconds into day, hours, mins, second
a = int(input("Enter the values in seconds : "))
se = a % 60
m = (a % 3600)// 60
h = (a % (24 * 3600)) /3600
d = (a /(24*3600))
print ("%d seconds = %d mins"  %(a, se))
print ("%d seconds = %d mins"  %(a, m))
print ("%d seconds = %d hours"  %(a, h))
print ("%d seconds = %d days"  %(a, d))
