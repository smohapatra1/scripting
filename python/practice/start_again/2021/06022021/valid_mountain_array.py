#Valid Mountain Array 
# 353 - > A mountain Array 
# 01321 - > Not an montain array 

def ma(nums):
    # Need minimum 3 inputs 
    if len(nums) <3:
        return False
    i = 1
    #Increasing hill
    while i < len(nums) and nums[i] > nums[i-1]:
        i+=1
    if i == 1 or i ==len(nums):
        return False
    #Decreasing hill
    while i < len(nums) and nums[i] < nums[i-1]:
        i+=1
    #Reached at the end of the array
    return i == len(nums)
   
nums = [1,2,5,4,2,1]
result = ma(nums)
print (result)