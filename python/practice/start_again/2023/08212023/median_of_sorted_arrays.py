# 4. Median of Two Sorted Arrays
# Hard
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

from typing import List
import statistics
def Median(nums1 : List[int], nums2: List[int]) -> float:
    # Solution-01
    # return statistics.median(nums1 + nums2)

    #Solution-02
    m=len(nums1)
    n=len(nums2)
    # An extra field 
    mid = (m+n )//2 + 1
    prev1 = None
    prev2 = None
    i = j = 0
    for _ in range (mid):
        prev2 = prev1 
        if j == n or (i !=m and nums1[i] <= nums2[j]):
            prev1 = nums1[i]
            i+=1
        else:
            prev1 = nums2[j]
            j+=1
    return prev1 if (m + n) % 2 else (prev1 + prev2 )/2

        
if __name__ == "__main__":
    nums1 = [1,3]
    nums2 = [2]
    # nums1 = [1,2]
    # nums2 = [3,4]
    print ("Median value is {}".format(Median(nums1, nums2)))