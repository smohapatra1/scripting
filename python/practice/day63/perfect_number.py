# perfect number

def perfect(x):
    for y in range(int(x)):
        sum = 1
        i = 2
        while i * i <=y:
            if y % i == 0:
                sum = sum + i + y/i
            i +=1
        if sum == y:
            print ( y, "is perfect" )
        else:
            print (y, "is not perfect")
    
perfect(input("Enter a number : "))
