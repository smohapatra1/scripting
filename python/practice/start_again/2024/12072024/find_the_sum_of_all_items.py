#   https://www.geeksforgeeks.org/python-program-to-find-the-sum-of-all-items-in-a-dictionary/

d = {'a' : 100, 'b': 200 , 'c': 1000}
sum = 0 
for i in d:
    sum = sum + d[i] 
print (sum)