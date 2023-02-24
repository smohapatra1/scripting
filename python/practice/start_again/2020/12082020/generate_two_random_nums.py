
#Problem 2
#Create a generator that yields "n" random numbers between a low and high number (that are inputs).
import random
random.randint(1,10)
def num(low,high,n):
    for i in range(n):
        yield random.randint(low,high)
for x in num(1,10,12):
    print (x)