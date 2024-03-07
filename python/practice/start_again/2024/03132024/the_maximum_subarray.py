# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-maxsubarray/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-four

# We define subsequence as any subset of an array. We define a subarray as a contiguous subsequence in an array.

# Given an array, find the maximum possible sum among:

# all nonempty subarrays.
# all nonempty subsequences.
# Print the two values as space-separated integers on one line.

# Note that empty subarrays/subsequences should not be considered.

# Example

# The maximum subarray sum is comprised of elements at inidices . Their sum is . The maximum subsequence sum is comprised of elements at indices  and their sum is .

# Function Description

# Complete the maxSubarray function in the editor below.

# maxSubarray has the following parameter(s):

# int arr[n]: an array of integers
# Returns

# int[2]: the maximum subarray and subsequence sums
# Input Format

# The first line of input contains a single integer , the number of test cases.

# The first line of each test case contains a single integer .
# The second line contains  space-separated integers  where .

# Constraints

# The subarray and subsequences you consider should have at least one element.

# Sample Input

# 2 
# 4 
# 1 2 3 4
# 6
# 2 -1 2 3 4 -5
# Sample Output

# 10 10
# 10 11
# Explanation

# In the first case:
# The max sum for both contiguous and non-contiguous elements is the sum of ALL the elements (as they are all positive).

# In the second case:
# [2 -1 2 3 4] --> This forms the contiguous sub-array with the maximum sum.
# For the max sum of a not-necessarily-contiguous group of elements, simply add all the positive elements.



def maxSubarray(arr):
    sum=[arr[0]]
    subsequene=arr[0] if arr[0] > 0 else 0
    for idx in range(1, len(arr)):
        sum.append(max(sum[idx-1] + arr[idx], arr[idx]))
        if arr[idx] > 0:
            subsequene +=arr[idx]
    maxValue=max(sum)
    return [maxValue, subsequene if maxValue > 0 else maxValue]


if __name__ == "__main__":
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)
        print (result)
