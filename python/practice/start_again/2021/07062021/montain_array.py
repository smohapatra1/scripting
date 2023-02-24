#Mountain Array 
# 353 - Mountain Array
#2135321 - Not a mountain array 

def ma(nums):
    if len(nums) < 3:
        return False
    i = 1 
    #Up hill
    while i < len(nums) and nums[i] > nums[i-1] :
        i +=1
    if i == 1 or i == len(nums):
        return False
    #Down hill    
    while i < len(nums) and nums[i] < nums[i-1]:
        i +=1
    return i == len(nums)
nums = [1,2,2,2]
result = ma(nums)
print (result)
