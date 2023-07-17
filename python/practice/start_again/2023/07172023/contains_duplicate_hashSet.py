#Find out duplicate from a list using hashset
#Using hashset

def containsDuplicate(nums):
    num=set()
    for i in nums:
        if i in num:
            return True
        num.add(i)
    return False

if __name__ == "__main__":
    nums=[1,2,3,4,2]
    if containsDuplicate(nums):
        print ("Contains Duplicate")
    else:
        print ("Doesn't contains Duplicate")