#!/usr/bin/python
#Covert tempratures
a = float(input("Enter the temp degree celcious : "))
k = float(a + 273.15)
f = float((a * 9)/5 + 32) 
print ("Temp in %f degree celcious is %f Kelvin" %(a , k))
print ("Temp in %f degree celcious is %f Farenheit" %(a , f))
a = float(input("Enter the temp degree Fahrenheit : "))
k = float(a - 32) * 5 / 9 + 273.15 
c = float((a -32) * 5 /9)
print ("Temp in %f degree Fahreinheat is %f K" %(a , k))
print ("Temp in %f degree Fahreinheat is %f C" %(a , c))
a = float(input("Enter the temp degree Kevlin : "))
c = float(a - 273.15 )
f = float(a - 273.15) *9 /5 + 32
print ("Temp in %f degree Kelvin is %f c" %(a , c))
print ("Temp in %f degree Kelvin is %f F" %(a , f))

