#What is the average of Sum of squares of integers from 1 to 5 ?
#from math import average
sum=0
for i in range(6):
    i = i ** 2
    print (f' i = {i}')
    sum = i + sum
#print (f' {average(sum)}')
average=sum/5
print (f' Sum = {sum} and \n Average = {average}')

