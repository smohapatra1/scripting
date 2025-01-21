#   https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/

import bisect

# initializing list
li1 = [1, 3, 4, 4, 4, 6, 7]
# initializing list
li2 = [1, 3, 4, 4, 4, 6, 7]
# initializing list
li3 = [1, 3, 4, 4, 4, 6, 7]

bisect.insort(li1, 5)
print ("The list after inserting new element using insort() is : ")
for i in range(0, 7):
    print(li1[i], end=" ")
bisect.insort_left(li2, 5)
print("\r")
 
print ("The list after inserting new element using insort_left() is : ")
for i in range(0, 7):
    print(li2[i], end=" ")
print("\r")

bisect.insort_right(li3, 5, 0, 4)
print ("The list after inserting new element using insort_right() is : ")
for i in range(0, 7):
    print(li3[i], end=" ")