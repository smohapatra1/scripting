# #   https://www.hackerrank.com/challenges/pairs/problem?isFullScreen=true

# Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.

# Example


# There are three values that differ by : , , and . Return .

# Function Description

# Complete the pairs function below.

# pairs has the following parameter(s):

# int k: an integer, the target difference
# int arr[n]: an array of integers
# Returns

# int: the number of pairs that satisfy the criterion
# Input Format

# The first line contains two space-separated integers  and , the size of  and the target value.
# The second line contains  space-separated integers of the array .

# Constraints

# each integer  will be unique
# Sample Input

# STDIN       Function
# -----       --------
# 5 2         arr[] size n = 5, k =2
# 1 5 3 4 2   arr = [1, 5, 3, 4, 2]
# Sample Output

# 3
# Explanation

# There are 3 pairs of integers in the set with a difference of 2: [5,3], [4,2] and [3,1]. .


def Pairs(k, arr):
    new_list = [ x + k for x in arr ]
    values = list(set(new_list) & set(arr))
    return len(values)

if __name__ == "__main__":
    new_input = input().rstrip().split()
    n = int(new_input[0])
    k = int(new_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = Pairs(k, arr)
    print (result)