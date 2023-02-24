#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
#count_primes(100) --> 25
def prime(a):
    for i in range(2,a):
        if i > 1:
            for j in range (2, i ):
                if i % j == 0 :
                    break
            else:
                print (i)
prime(100)