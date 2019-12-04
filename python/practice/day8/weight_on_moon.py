#!/usr/bin/python
#The weight of a person on the moon is 1/6th the weight of a person standing on earth. Say that your weight on earth increases by 1 kg every year. Write a program that will print your weight on the moon every year for the next 10 years. (Your initial weight can be anything.)
pweight = 60
counter = 0 
#pweight_on_moon = (pweight/6) *100
for i in range(0,10):
    pweightmoon = pweight/6
    print ("Counter -%d %s" % ( counter , float(pweightmoon)))
    pweight = pweight + 1
    counter = counter + 1
