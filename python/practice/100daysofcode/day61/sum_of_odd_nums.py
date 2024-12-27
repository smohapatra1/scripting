#find sum of odd numbs from list

def sum_of_odd(x):
    l = x.split()
    print ("The numbers are " , l)
    sum = 0 
    for y in l :
        if int(y) % 2 == 1 :
            sum += int(y)
    print ("sum - ", sum)

sum_of_odd(input("Enter lists with spaces : "))
