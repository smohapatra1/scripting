# 42. Trapping Rain Water

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

# Example 1:


# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
# Example 2:

# Input: height = [4,2,0,3,2,5]
# Output: 9

# Solution 
#   


def trapping_rain_water(height):
    #BFM 
    n = len(height)
    water=0
    for i in range(n):
        j=i
        left_max=0
        right_max=0
        while j >=0:
            left_max=max(left_max, height[j])
            j-=1
        j=i
        while j <n:
            right_max=max(right_max, height[j])
            j+=1
        water+=min(left_max, right_max) - height[i]
    return water


    # #- two pointer method 
    # #Initialise everything
    # n=len(height)
    # left=0
    # right=n-1
    # left_max=height[left]
    # right_max=height[right]
    # water=0
    # while left < right:
    #     left_max=max(left_max, height[left])
    #     right_max=max(right_max, height[right])
    #     if left_max <=right_max:
    #         water+=left_max -height[left]
    #         left+=1
    #     else:
    #         water+=right_max-height[right]
    #         right-=1
    # return water


  
if __name__ == "__main__":
    height=[4,2,0,3,2,5,6]
    #height=[0,1,0,2,1,0,1,3,2,1,2,1]
    print ("The total number of water can be trapped is {}".format(trapping_rain_water(height)))
