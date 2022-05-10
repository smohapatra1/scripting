#Check if a number is prime : True/False
def is_prime(n):
    for i in range(2,n):
        if n %i == 0:
            print (f"{n} is prime")
        else:
            print (f"{n} is not prime")
is_prime(int(input("Enter the number: ")))
