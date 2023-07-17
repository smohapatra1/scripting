#Find a duplicate entry from the list of array
#Using Sorting

def containsDuplicate(nums):
    n=len(nums)
    nums.sort()
    for i in range (1,n):
        if nums[i] == nums[i-1]:
            return True
    return False

if __name__ == "__main__":
    nums=[1,2,3,1,1,2,3]
    if containsDuplicate (nums):
        print ("Duplicate exists")
    else:
        print ("Duplicate doesn't exist")