#!/usr/bin/python
#Write a program that asks the user to enter a positive integer n. Assuming that this integer is in seconds, your program should convert the number of seconds into days, hours, minutes, and seconds and prints them exactly in the format specified below. Here are a few sample runs of what your program is supposed to do: 

a = int(input('Enter the seconds : '))
day = a // (24 * 3600)
hours = (a % (24 * 3600  )) / 3600
minutes = ( a % 3600 ) //60
second = ( a % 60 )
print ('%d days %d hours %d minutes %d seconds' %(day, hours, minutes, second))
