#Move 0 to the end in an array

def move_zero(nums):
    i = 0 
    n = len(nums)
    for num in nums:
        if num != 0:
            nums[i] = num
            i+=1
    for x in range(i,n):
        nums[x] = 0
    print (nums)
nums = [1,0,2,3,0]
move_zero(nums)