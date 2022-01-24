#Ask an user to enter a number. Find out if this number is Odd or Even 
def odd_even(n):
    if n > 0:
        if n %2 == 0 :
            print (f'{n} is even')
        else:
            print (f'{n} is odd')
odd_even (int(input("Enter the number : ")))