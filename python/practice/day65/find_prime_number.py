# Type your code here
def prime(x):
    for i in range(2, x):
        j = 2
        counter = 0 
        while j < i :
             if i % j == 0:
                j +=1
                counter = 1
             else:
                j +=1
        if counter == 0 :
            print(i, "is Prime")
        else:
           counter =0

prime(int(input("Enter a number ")))
