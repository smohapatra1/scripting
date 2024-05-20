#   Print a Fibonacci series using recursion?

def fibo_rec(n):
    if n <= 1:
        return n 
    else:
        return (fibo_rec(n-1) + fibo_rec(n-2))
nterms = 10 
if nterms <=0 :
    print ("Please enter positive integers")
else:
    print ("Fibonacci Sequence:")
    for i in range(nterms):
        print (fibo_rec(i))
