#Zero Move 
#Given an array of integrers , write a function to move all 0's to the end
#while maintaining the relative order of the other elements 

# Move the non-zero elements to the begining of the array 
# keep track of their counts including the number of zeros 

def move_zero(nums):
    i = 0 
    n = len(nums)
    for num in nums:
        if num != 0 :
            nums[i] = num
            i+=1
    for x in range(i,n):
        nums[x] = 0
    print (nums)
nums = [0,0,0,7,4,2,3,4,5,0,0,100,0,123,1,0,3,12]
move_zero(nums)