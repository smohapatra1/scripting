#Zero move to end 
# 

def non_zero(nums):
    i = 0 
    n = len(nums)
    for num in nums:
        if num != 0:
            nums[i] = num
            i +=1
    for x in range (i,n):
        nums[x] = 0
    print (nums)
nums = [ 1,2,3,4,5,0,4,0,2,1]
result = non_zero(nums)