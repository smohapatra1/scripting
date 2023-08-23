# 84. Largest Rectangle in Histogram
# Hard

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

# Example 1:


# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.
# Example 2:


# Input: heights = [2,4]
# Output: 4


# Solution 
#   Idea to use Monotonic Stack
#   Iterate over bars
#   Add them into a stack if last element in the stack is less than current bar
#   If the above condition doesn't hold true, calculate area by poping out bars from stack
#   Area = (Number of pops * current height )


def LargeRecHis(heights):
    #Solution-01 
    # stack=[]
    # result=0
    # for height in heights + [-1]: # To have an additional iteration 
    #     step=0
    #     while stack and stack[-1] [1] >=height:
    #         w , h = stack.pop()
    #         step +=w
    #         result = max(result, step * h)
    #     stack.append((step +1, height))
    # return result

    #Solution-02
    heights.append(0)
    stack=[-1]
    result = 0 
    for i in range(len(heights)):
        while heights[i] < heights[stack [-1]]:
            height = heights [stack.pop()]
            width = i - stack[-1] -1
            result = max (result, height * width)
        stack.append(i)
    return result 




if __name__ == "__main__":
    #heights = [2,1,5,6,2,3]
    heights = [2,4]
    print ("Result = {}".format(LargeRecHis(heights)))


