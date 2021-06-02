#Conatiner with the most water 
# Given and array with non-negative integers 
import pdb
def water(height):
    l = 0 
    r = len(height) - 1
    maxarea = 0 
    while l < r :
        # r -l = x axis
        # minimum values of two containers ( height of the container) = y axis 
        maxarea = max(maxarea, min(height[l],height[r]) * (r-l))
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
    return maxarea 
height = [1,8,6,2,5,4,8,3,7]
result = water(height)
print (result)