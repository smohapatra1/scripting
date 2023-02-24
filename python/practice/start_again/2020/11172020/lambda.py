mynum = [1,2,3,4]
#Getting Squares 
print (list(map(lambda num:num ** 2,mynum)))
#Getting Even Numbers 
print (list(filter(lambda num:num %2==0, mynum)))