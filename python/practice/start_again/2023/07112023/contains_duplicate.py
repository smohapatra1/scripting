#https://leetcode.com/problems/contains-duplicate/
#Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.


def containsDuplicate(self, nums: List[int]) -> bool:
    s=set(nums)
    if len(s) == len(nums):
        return False
    else:
        return True 
    
if __name__ == "__main__":
    List=[1,2,3,4]
    if containsDuplicate(List):
        print ("Duplicate Exist")
    else:
        print ("Duplicate doesn't exist")
        


