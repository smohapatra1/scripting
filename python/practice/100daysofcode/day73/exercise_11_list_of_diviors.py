#List Methods Exercise 11 (List of Divisors)
#Write a function that accepts a positive integer k and returns the list of all the divisors of k. Your list should include both 1 and k.
def divisor(x):
    list=[]
    if x > 0:
        for i in range (1,x+):
            if x % i == 0:
                list.append(i)
        print (list)
divisor(int(input("Enter a value ")))
        
