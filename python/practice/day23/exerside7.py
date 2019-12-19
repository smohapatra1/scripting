#!/usr/bin/python
#Write a program which asks the user to enter a positive integer 'n' (Assume that the user always enters a positive integer) and based on the following conditions, prints the appropriate results exactly as shown in the following format (as highlighted in yellow).
#when 'n' is divisible by both 2 and 3 (for example 12), then your program should print
a = int(raw_input("Enter a positive Integer : "))
if a % 2 == 0 and a % 3 == 0:
    print ('BOTH')
elif a % 2 == 0 or a % 3 == 0:
    print ('ONE')
elif a % 2 != 0 and a % 3 != 0:
#else:
    print ('NEITHER')
