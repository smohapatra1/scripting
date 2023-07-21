#Two Sum :- 

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

#   Steps 
#   Define the array of integers - nums
#   Define another integer - target 
#   Get the two integers
#   Added the two integers 
#   Go until its end and return the Sum of two integers


#BFM 

def twoSum(nums,target):
    n=len(nums)
    required={}
    for i in range(n):
        for j in range(i+1, n ):
            if nums[j] == target - nums[i]:
                return [i, j] 
                #print ("The fields are {},{} and values are {} + {} = {}".format(i , j, nums[i], nums[j],target))
    return False

if __name__ == "__main__":
    nums=[1,2,3,5,8,10]
    target=3
    print ("The nums are {} & Target is {}".format(nums, target))
    print ("The Number positions for the target are {}".format(twoSum(nums,target)))