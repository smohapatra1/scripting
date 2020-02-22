'''
https://courses.edx.org/courses/course-v1:UTArlingtonX+CSE1309x+1T2018/courseware/e3b7d74dca244a08b208d1f4b68e49e0/d3906c7bc4234b25a8c0ad53e8be0bbd/?child=first

Quiz 3, Part 8 (Find number of chickens and dogs function)
Bookmark this page
Quiz 3, Part 8
0.0/10.0 points (graded)
Write a function that accepts two positive integers as parameters. The first integer is the number of heads and the second integer is the number of legs of all the creatures in a farm which consists of chickens and dogs. Your function should calculate and return the number of chickens and number of dogs in the farm in a list as specified below. If it is impossible to determine the correct number of chickens and dogs with the given information then your function should return None. 

Example 1, if your function received the following numbers:

5, 12 
This means that someone has counted a total of 5 heads and total of 12 legs in the farm. Now, your function should calculate how many chickens and how many dogs are in the farm and return that information in a list exactly as shown below.

[4, 1] 

this means that there were 4 chickens and 1 dog in the farm. 

Example 2, if your function received the following numbers:
7, 12 
Then it should return:
None 
'''

def solve(num_legs, num_heads):
    for num_chi in range(0, num_heads+1):
        num_dogs = num_heads - num_chi
        total_legs = 4 * num_dogs + 2 * num_chi
        if total_legs == num_legs:
            return [num_dogs , num_chi]
    return [None, None]
def animal(heads,legs):
    dogs, chi = solve(legs,heads)
    if dogs == None :
        print ("No solutions")
    else:
        print ("Num of dogs - ", dogs)
        print ("Num of chi - ", chi)

animal(int(input("Enter Number of animal heads : ")), int(input("Enter Number of legs : ")))

