
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

# Don't refer this until you coded yourself - https://www.enjoyalgorithms.com/blog/product-of-array-except-self 


# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

#BFM 
# def ProductExceptSelf(X):
#     product=[0] * n 
#     for i in range(n):
#         ProductofSelf=1
#         for j in range(n):
#             if i == j:
#                 continue
#             ProductofSelf=ProductofSelf*X[j]
#         product[i]=ProductofSelf
#     return product

#Using Prefix and Suffix product Array

def ProductExceptSelf(X):
    product=[0] * n 
    product[0] = 1
    for i in range(1,n):
        product[i] = X[i-1] * product[i-1]
    suffixProduct=1
    for i in range(n-1, -1, -1 ):
        product[i]=product[i]*suffixProduct
        suffixProduct=suffixProduct * X [i]
    return product

if __name__ == "__main__":
    X=[0,2,3,4]
    n=len(X)
    print ("Current elements : {}".format(X))
    print ("Product of array except self: {}".format(ProductExceptSelf(X)))
