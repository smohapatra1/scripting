# #   https://www.hackerrank.com/challenges/unbounded-knapsack/problem?isFullScreen=true

# Given an array of integers and a target sum, determine the sum nearest to but not exceeding the target that can be created. To create the sum, use any element of your array zero or more times.

# For example, if  and your target sum is , you might select  or . In this case, you can arrive at exactly the target.

# Function Description

# Complete the unboundedKnapsack function in the editor below. It must return an integer that represents the sum nearest to without exceeding the target value.

# unboundedKnapsack has the following parameter(s):

# k: an integer
# arr: an array of integers
# Input Format

# The first line contains an integer , the number of test cases.

# Each of the next  pairs of lines are as follows:
# - The first line contains two integers  and , the length of  and the target sum.
# - The second line contains  space separated integers .

# Constraints



# Output Format

# Print the maximum sum for each test case which is as near as possible, but not exceeding, to the target sum on a separate line.

# Sample Input

# 2
# 3 12
# 1 6 9
# 5 9
# 3 4 4 4 8
# Sample Output

# 12
# 9
# Explanation

# In the first test case, one can pick {6, 6}. In the second, we can pick {3,3,3}.

T = int(input())

for i in range(T):
    n,k = list(map(int,input().split(' ')))
    nums=list(map(int,input().split(' ')))
    p=[-1 for j in range(k+1)]
    p[0] = 0
    max=0
    for j in range(k+1):
        if (p[j] > -1):
            for num in nums:
                if(j+num <= k):
                    p[j+num] = j
                    if (j+num > max):
                        max=j+num
    print(max)