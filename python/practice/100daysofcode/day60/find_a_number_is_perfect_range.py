#Find the perfect from range
def perfect(x):
    for y in range (int(x)):
        sum = 1
        i = 2
        while i * i <= int(y):
            if int(y) % i == 0 :
                sum = sum + i + int(y)/i
            i +=1
        if sum == y:
            print (y, "is perfect")
        else:
            print (y, "NOT perfect")
perfect(input("Enter the range : "))

