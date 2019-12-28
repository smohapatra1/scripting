#!/usr/bin/python
#Find the square root of a number
a = int(input("Enter a number : "))
guess = a /2
f = abs(a - (a ** 2 ))
accuracy = 0.01
while f > accuracy :
    guess= (guess + (a/guess))/2
    print ("Original number % d" % a)
print ("Square root of %d is % d"  % (a, guess ))
