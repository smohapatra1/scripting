#sum of add numbers from fun
def odd(x):
    y= x.split()
    print (y)
    sum = 0 
    for i in y:
        if int(i) % 2 == 1:
            sum = sum + int(i) 
    print (sum)

odd(input("Enter the numbers with space : "))
