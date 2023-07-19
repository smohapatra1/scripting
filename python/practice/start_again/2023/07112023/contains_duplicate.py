#https://leetcode.com/problems/contains-duplicate/
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

#Check Duplicate 

#BFM Method 
# def containsDuplicate(nums):
#     for i in range(n):
#         for j in range (i+1, n ):
#             if nums[i] == nums[j]:
#                 return True
#     return False

# Sorting Method
# def containsDuplicate(nums):
#     nums.sort()
#     for i in range (1,n):
#         if nums[i] == nums[i-1]:
#             return True
#     return False 

#Set Method 
def containsDuplicate(nums):
    num=set()
    for i in nums:
        if i in num:
            return True
        num.add(i)
    return False        

if __name__ == "__main__":
    nums=[1,2,3,4]
    n=len(nums)
    if containsDuplicate(nums):
        print ("Duplicate exist")
    else:
        print ("Duplicate doesn't exist")
        


