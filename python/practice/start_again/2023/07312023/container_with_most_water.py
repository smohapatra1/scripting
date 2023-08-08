# 11. Container With Most Water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Solution:- 
#   1. Find the two pointers - left and right and initialize them 
#   2. Initialize MaxArea
#   3. If left < right 
#   4. Get the Current Area :- Min Area CurrentArea ( From left and right ) and multiply the minimum height by the width ( right - left  )
#   5. Find the MaxArea from currentArea and MaxArea
#   6. if left height is less than right height , increment left else decrement right
#   7. Now return Max Area   


def MaxArea(height):
    left=0
    right= len(height) -1 
    MaxArea=0
    while left < right :
        currentArea = min(height[left], height[right]) * (right - left )
        MaxArea =max (currentArea, MaxArea)
        if height[left] < height[right]:
            left +=1
        else:
            right -=1
    return MaxArea


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print ("Max Area is {}".format(MaxArea(height)))

