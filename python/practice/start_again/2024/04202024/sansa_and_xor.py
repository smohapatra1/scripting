# #   https://www.hackerrank.com/challenges/sansa-and-xor/problem?isFullScreen=true

# Sansa has an array. She wants to find the value obtained by XOR-ing the contiguous subarrays, followed by XOR-ing the values thus obtained. Determine this value.

# Example

# Subarray	Operation	Result
# 3		None		3
# 4		None		4
# 5		None		5
# 3,4		3 XOR 4		7
# 4,5		4 XOR 5		1
# 3,4,5		3 XOR 4 XOR 5	2
# Now we take the resultant values and XOR them together:

# . Return .

# Function Description

# Complete the sansaXor function in the editor below.

# sansaXor has the following parameter(s):

# int arr[n]: an array of integers
# Returns

# int: the result of calculations
# Input Format

# The first line contains an integer , the number of the test cases.

# Each of the next  pairs of lines is as follows:
# - The first line of each test case contains an integer , the number of elements in .
# - The second line of each test case contains  space-separated integers .

# Constraints




# Sample Input 0

# 2
# 3
# 1 2 3
# 4
# 4 5 7 5
# Sample Output 0

# 2
# 0
# Explanation 0

# Test case 0:


# Test case 1:

# Sample Input 1

# 2
# 3
# 98 74 12
# 3
# 50 13 2
# Sample Output 1

# 110
# 48
# Explanation 1

# Test Case 0:


# Test Case 1:

def getXor(lst):
    res = 0 
    for i in range(0, len(lst), 2):
        res ^=lst[i]
    return res

def sansaXor(arr):
    if len(arr) % 2 == 0 :
        return 0
    return getXor(arr)


if __name__ == "__main__":
    t = int(input().strip())
    for t_iter in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        result = sansaXor(arr)
        print (result)