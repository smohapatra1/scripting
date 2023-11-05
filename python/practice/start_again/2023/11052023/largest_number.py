# #   https://leetcode.com/problems/largest-number/

# 179. Largest Number
# Medium
# 7.7K
# 606
# Companies
# Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

# Since the result may be very large, so you need to return a string instead of an integer.

 

# Example 1:

# Input: nums = [10,2]
# Output: "210"
# Example 2:

# Input: nums = [3,30,34,5,9]
# Output: "9534330"

from typing import List
def largest_number(nums: List[int]) -> int:
    return str(int(''.join(sorted(map(str, nums), key=lambda s:s*9)[::-1])))

if __name__ == "__main__":
    #nums = [10,2]
    nums = [3,30,34,5,9]
    print ("The largest number is : {}".format(largest_number(nums)))
