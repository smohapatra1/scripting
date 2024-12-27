#Write a function that accepts a list of integers as parameter. Your function should return the sum of all the odd numbers in the list. If there are no odd numbers in the list, your function should return 0 as the sum. 

#Remember that you are not asked to print anything. So, your function should just return the sum of all the odd numbers in the list. You do not need to call your function, it will automatically be called and tested for correctness with the test cases we provide. You only need to write one function and we will test your program with the first function that appears in your code. So, if you want to write more than one function to help you solve the problem, remember to embed the helper functions inside the first function.
#https://courses.edx.org/courses/course-v1:UTArlingtonX+CSE1309x+1T2018/courseware/e3b7d74dca244a08b208d1f4b68e49e0/d3906c7bc4234b25a8c0ad53e8be0bbd/?child=first
import os
def sum_of_odd(x):
    y = x.split()
    print("Entered values" , y)
    sum = 0 
    for i in y:
        #print ("i = " , i)
        if int(i) % 2 == 1:
            sum += int(i)
        #else:
        #    print ("0")
    print("Odd Sum", sum)
        
'''
        if i % 2 != 0:
            print (i)
            sum = i + i
        print (sum)
'''


sum_of_odd(input("Enter the list with sapces :"))
