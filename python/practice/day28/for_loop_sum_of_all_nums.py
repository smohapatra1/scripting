#/usr/bin/python
#Using a for loop, write a program which asks the user to type an integer, n, and then prints the sum of all numbers from 1 to n (including both 1 and n).
a = int(input("Enter a number : "))
count = 0 
for i in range( count, a):
    i +=1
    count = count + i 
print (count)
