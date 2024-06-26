# #   https://www.hackerrank.com/challenges/minimum-distances/problem?isFullScreen=true

# The distance between two array values is the number of indices between them. Given , find the minimum distance between any pair of equal elements in the array. If no such value exists, return .

# Example

# There are two matching pairs of values:  and . The indices of the 's are  and , so their distance is . The indices of the 's are  and , so their distance is . The minimum distance is .

# Function Description

# Complete the minimumDistances function in the editor below.

# minimumDistances has the following parameter(s):

# int a[n]: an array of integers
# Returns

# int: the minimum distance found or  if there are no matching elements
# Input Format

# The first line contains an integer , the size of array .
# The second line contains  space-separated integers .

# Constraints

# Output Format

# Print a single integer denoting the minimum  in . If no such value exists, print .

# Sample Input

# STDIN           Function
# -----           --------
# 6               arr[] size n = 6
# 7 1 3 4 1 7     arr = [7, 1, 3, 4, 1, 7]
# Sample Output

# 3
# Explanation
# There are two pairs to consider:

#  and  are both , so .
#  and  are both , so .
# The answer is .

def minimumDistance(a):
    b = len(a)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if a[i] == a[j]:
                distance = abs(i - j)
                b = min(b, distance)
    if b==len(a):
        return -1
    else:
        return b

if __name__ == "__main__":
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    result = minimumDistance(a)
    print (result)