# 238. Product of Array Except Self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]


def productExceptSelf(X):
    product=[0] * n 
    for i in range(n):
        productExclCurrent=1
        for j in range(n):
            if i == j:
                continue
            productExclCurrent = productExclCurrent*X[j]
        product [i] = productExclCurrent
    return product

if __name__ == "__main__":
    X=[0,2,3,4]
    n=len(X)
    print ("Current Numbers : {}".format(X))
    print ("Products of Numbers : {}".format(productExceptSelf(X)))
