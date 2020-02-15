def perfect(x):
        sum = 1
        i = 2
        while i * i <=x:
              if x % i == 0:
                 sum = sum + i + x/i
              i +=1
        if sum == x:
           print (x, "is perfect")
        else:
           print (x, "is NOT perfect")
    

perfect(int(input("input a number : ")))
