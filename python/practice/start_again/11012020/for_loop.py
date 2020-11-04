#Print the loop
#for loop
i = [1,2,3,4,5,6,7,8,9,10]
for n in i :
    print (n)
    #Print Even Number
    if n %2 == 0:
        print ("Print even Number {}".format(n))
    #Print Odd Number
    else:
    #if n % 2 != 0:
        print ("Print odd number {}".format(n))
    #Sum of all numbers 
    sum=0
    for n in i:
        sum=sum+n
    print (sum)
    