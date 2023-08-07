# 167. Two Sum II - Input Array Is Sorted

# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Solution :- 
#   1. Initialize two pointers i and j 
#   2. Add elements pointed by i and j and then compare with target 
#   3. If target is smaller, it means you have added a larger element and it needs to be cutoff, decrement j
#   4. if target is larger, it means you have added a smaller element and it needs to pick the big value, increment i
#   5. Repeat 2 and 4 until i >=j or  match is found 


def two_sum(arr,target):
    i = 0 # First element 
    j = ( len(arr) - 1)  # Last element 
    while arr [i] + arr [j] != target:
        s = arr [i] + arr [j]
        if s > target:
            j -=1
        else:
            i +=1
    return [ i+1, j +1 ]
    # return [ i+1, j +1 ] 
    # for i in range(l):
    #     for j in range (i+1, l):
    #         if arr[j] == target - arr [i]:
    #             return [i, j]
    # return False

if __name__ == "__main__":
    arr = [ 1, 2, 3, 4 ]
    target = 8
    print ("the target is {}".format(two_sum(arr, target)))