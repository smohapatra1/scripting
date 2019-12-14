#!/usr/bin/python
#Write a program that asks the user for a positive integer between 1 and 7 (Assume that the user may enter any number from 1 to 7 both inclusive) and prints the day of week corresponding to that number in all capital letters. Assume that the day of the week starts from MONDAY. For example: if the user enters:
try:
    x=1
    while x<7:
        dayofweek1 = [ "Not a day", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        dayofweek = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
        y = int(input("Enter the day :"))
        print ("%s" % dayofweek[y-1])
        print ("%s" % dayofweek1[y])
        break
except:
    print ("Days are outisde of the week")
