# #   https://leetcode.com/problems/merge-sorted-array/

# 88. Merge Sorted Array
# Easy
# 13.2K
# 1.5K
# Companies
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.


from typing import List
def merge(nums1: List[int], nums2: List[int], m: int, n:int) -> List[int]:
    #Solution-01

    # for i in range(m, m+n):
    #     nums1[i] = nums2[i-m]
    # return nums1.sort()
    
    #Solution-02

    # nums1[m:] = nums2
    # nums1.sort()

    # Solution-03
    idx=0
    for i in range(len(nums1)):
        if idx >=n:
            break
        if nums1[i] == 0:
            nums1[i]=nums2[idx]
            idx+=1
    nums1.sort()

if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    print ("{}".format(merge(nums1, nums2, m, n)))