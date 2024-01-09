# #   https://leetcode.com/problems/longest-turbulent-subarray/

# 978. Longest Turbulent Subarray
# Medium
# 1.9K
# 216
# Companies
# Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

# A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

# More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

# For i <= k < j:
# arr[k] > arr[k + 1] when k is odd, and
# arr[k] < arr[k + 1] when k is even.
# Or, for i <= k < j:
# arr[k] > arr[k + 1] when k is even, and
# arr[k] < arr[k + 1] when k is odd.
 

# Example 1:

# Input: arr = [9,4,2,10,7,8,8,1,9]
# Output: 5
# Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
# Example 2:

# Input: arr = [4,8,12,16]
# Output: 2
# Example 3:

# Input: arr = [100]
# Output: 1


from typing import List
def LongestTurbulentArray( arr : List[int]) -> int:
    n=len(arr)
    l=0
    r=0
    ans=1
    if n == 1:
        return 1
    while r < n:
        while l < n-1 and arr[l] == arr[l+1]:
            l+=1
        while r < n-1 and (arr[r-1] > arr[r] < arr[r+1] or arr[r-1] < arr[r] > arr[r+1]):
            r +=1
        ans=max(ans, r - l+1)
        l=r
        r+=1
    return ans
    


if __name__ == "__main__":
    arr = [9,4,2,10,7,8,8,1,9]
    print ("{}".format(LongestTurbulentArray(arr)))