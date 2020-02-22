def prime(x):
    for i in range(2, x):
        j = 2
        counter = 0 
        while j < i :
            #print (i, j)
            if i % j == 0:
                counter = 1
                j += 1
            else:
                j +=1
        if counter == 0 :
            print (i, "is prime")
        else:
            counter = 0 
            print (i, "NOT prime")

prime(int(input("Enter a number ")))
