#Contains Duplicate - various forms 
#https://lifewithdata.com/2023/06/12/leetcode-contains-duplicate-solution-in-python/

#Brute Force Method
def containsDuplicate(nums):
    n=len(nums)
    for i in range(n):
        for j in range(i+1, n ):
            if nums[i] == nums[j]:
                return True
    return False

if __name__ == "__main__":
    nums=[1,2,3,4,5]
    if containsDuplicate(nums):
        print ("Duplicate Exists")
    else:
        print ("Duplicate Doesn't Exist")    



