#   Write a Python program to count the frequency of each element in a list.

def FreqCount(nums):
    count = {}
    for i in nums:
        if i in count:
            count[i] +=1
        else:
            count[i] = 1
    return count

if __name__ == "__main__":
    nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
    result = FreqCount(nums)
    print (result)