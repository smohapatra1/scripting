#   How would you implement Binary Search?


def BinarySearch(nums, target):
    for i, l in enumerate(nums):
        if target == l:
            return i
    return -1

if __name__ == "__main__":
    nums = [-1,0,3,5,9,12] 
    target = 12
    result = BinarySearch(nums, target)
    print (result)