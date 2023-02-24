#Containers with most water 

def maxwater(height):
    l = 0 
    r = len(height) - 1 
    maxarea = 0 
    while l < r :
        # r-l = X-Asis or distance between two containers
        #minimum values of two containers = Y-Axis
        maxarea = max(maxarea, min(height[l], height[r]) * (r-l))
        if height[l] < height[r]:
            l+=1
        else:
            r-=1
    return maxarea
height=[1,2,3,4,5]
result = maxwater(height)
print (result)