def check_even(x):
    return x%2 ==0
my_num= [1,2,3,4,5,6]
print (list(filter(check_even, my_num)))