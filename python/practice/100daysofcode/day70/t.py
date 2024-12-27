def multiples(x):
    list=[]
    for k in range(1,x+1):
        multi = k * x 
        list.append(multi)
    print (list)
multiples(int(input("Enter a number ")))
