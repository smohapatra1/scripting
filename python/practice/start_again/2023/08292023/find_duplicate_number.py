# 287. Find the Duplicate Number
# Medium
# Companies
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3

# Solution -01
def FindDupe(nums):
    #Solution-01
    # l=len(nums)-1
    # seen = [0] * (l+1)
    # for num in nums:
    #     if seen[num]:
    #         return num
    #     seen[num]=1
    #Solution-02
    for n in nums:
        n=abs(n)
        if nums[n] < 0:
            return n
        nums[n] *= -1

if __name__ == "__main__":
    nums = [3,1,3,4,2]
    print ("The duplicate number is {}".format(FindDupe(nums)))