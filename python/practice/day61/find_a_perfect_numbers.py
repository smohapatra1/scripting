#Find a perfect number :- 
def perfect(x):
    for y in range(int(x)):
        #print (y)
        sum = 1
        i = 2
        while i * i <= y :
            if y % i == 0:
                sum = sum + i + y/i
            i +=1
        #print ("sum and y ",  (sum , y)) 
        if sum == y:
            print(y , "is a Perfect")
        else:
            print(y, "is NOT perfect")

perfect(input("Enter a number for range : "))
