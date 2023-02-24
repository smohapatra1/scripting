#Create a generator that generates the squares of numbers up to some number N.
def square(n):
    for x in range(n):
        yield x**2
for num in square(10):
    print ("Square of {} ".format(num))
