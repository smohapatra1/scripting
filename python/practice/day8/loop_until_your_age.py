#!/usr/bin/python
#Create a loop that prints out either even numbers, or odd numbers all the way up till your age. Ex: 2,4,6,....,14
age = int(raw_input("Enter your age: "))
for i in range(0,age, 2):
        print ("%d is a even number") % i 
