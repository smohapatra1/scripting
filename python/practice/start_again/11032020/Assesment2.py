
#Use range() to print all the even numbers from 0 to 10.
for i in range (0,10):
    if i % 2 ==0:
        print (i)
#Method 2
mylist=[x for x in range(0,10) if x % 2 == 0 ]
print (mylist)