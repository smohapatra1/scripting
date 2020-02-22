#Write a function that accepts a positive integer n as function parameter and returns True if n is a prime number, False otherwise. Note that zero and one are not prime numbers and two is the only prime number that is even. 

#Remember that you are not asked to print anything. So, your function should return either True or False and not print it. You do not need to call your function, it will automatically be called and tested for correctness with the test cases we provide. You only need to write one function and we will test your program with the first function that appears in your code. So, if you want to write more than one function to help you solve the problem remember to embed the helper functions inside the first function.
#Prime number is divisible by 1 or its own
def prime(x):
    if x <= 0:
        return False
    for i in range(1, x):
        if x % i == 0:
            #return False
            print (i, "is prime ")
        #else:
            #return True
        #    print (i, "NOT prime")

prime(int(input("Enter a number : ")))
