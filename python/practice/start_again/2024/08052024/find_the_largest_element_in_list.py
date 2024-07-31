#   Question 3: Write a Python program to find the largest element in a list.


def LargestElement(nums):
    large = nums[0]
    for n in nums:
        if n > large :
            large = n 
    return large
            
if __name__ == "__main__":
    nums = [10, 5, 8, 20, 50]
    result = LargestElement(nums)
    print (result)