#Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
mylist=[x for x in range(1,50) if x % 3 == 0]
print (mylist)