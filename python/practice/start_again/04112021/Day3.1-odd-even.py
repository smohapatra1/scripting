## Odd or Even

# Instructions

#Write a program that works out whether if a given number is an odd or even number. 

#Even numbers can be divided by 2 with no remainder. 

#e.g. 86 is **even** because 86 ÷ 2 = 43

#43 does not have any decimal places. Therefore the division is clean.

#e.g. 59 is **odd** because 59 ÷ 2 = 29.5

#29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
number=float(input("Enter a number: "))
if number % 2 == 0 :
    print ("%d is an even number" % number)
else:
    print ("%d is an odd number" % number)
