#!/usr/bin/python
#Find a prime number from a range
s = int(input("Enter a start number : "))
e = int(input("Enter a end number : "))
for num in range (s, e):
    if num > 1 :
        for i in range(2, num ):
            if (num % i) == 0:
                #print ("%d is not prime" % i)
                break
        else:
            print ("%d is prime" %num)
    #else:
    #    print ("%d is not prime" % num)
