#!/usr/bin/python
#Program to convert temperature from degree Celsius to Kelvin
a = int(input("Enter the temprature in degree celcious: "))
k = float(a + 273.15 )
f = float((a * 9)/5 + 32)
print ('Degree C - in F > %f ' % f)
print ('Degree C - in K > %f ' % k)
