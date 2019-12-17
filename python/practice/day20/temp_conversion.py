#!/usr/bin/python
#Convert Farenheat to Celcious
a =int(raw_input("Enter the temp: "))
celcius = float(((a *9)/9)+32)
if celcius > 90 :
    print ("Its very hot")
else:
    print ("Its Cold")
print (celcius)

