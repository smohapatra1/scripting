#Write a function which accepts an input list of numbers and returns the smallest number in the list (Do not use python's built-in min() function).
# get the numbers - 
def min_num(n):
    my_min= n[0] 
    for i in n:
        if i < my_min:
            my_min = i
    print ("Minimum number is %d from %s " % (my_min,  n))
min_num(input("Enter the numbers in list form "))
