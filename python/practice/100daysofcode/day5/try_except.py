#!/usr/bin/python
#Try- except
try:
    c = int(raw_input("Enter a number: "))
    if c >= 5 :
        print ("%d is a large number") % c
except:
    print ("%d is a small number") % c
finally:
    print ("%d is Nutral") % c
