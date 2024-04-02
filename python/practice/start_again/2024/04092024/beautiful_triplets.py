# #   https://www.hackerrank.com/challenges/beautiful-triplets/problem?isFullScreen=true

# Given a sequence of integers , a triplet  is beautiful if:

# Given an increasing sequenc of integers and the value of , count the number of beautiful triplets in the sequence.

# Example


# There are three beautiful triplets, by index: . To test the first triplet,  and .

# Function Description

# Complete the beautifulTriplets function in the editor below.

# beautifulTriplets has the following parameters:

# int d: the value to match
# int arr[n]: the sequence, sorted ascending
# Returns

# int: the number of beautiful triplets
# Input Format

# The first line contains  space-separated integers,  and , the length of the sequence and the beautiful difference.
# The second line contains  space-separated integers .

# Constraints

# Sample Input

# STDIN           Function
# -----           --------
# 7 3             arr[] size n = 7, d = 3
# 1 2 4 5 7 8 10  arr = [1, 2, 4, 5, 7, 8, 10]
# Sample Output

# 3
# Explanation

# There are many possible triplets , but our only beautiful triplets are  ,  and  by value, not index. Please see the equations below:




# Recall that a beautiful triplet satisfies the following equivalence relation:  where .

def beautifulTriplets(d, arr):
    s = set(arr)
    count = 0 
    for i in range(len(arr)-2):
        if arr[i]+d in s and arr[i]+2*d in s:
            count +=1
    return count

if __name__ == "__main__":
    first_input=input().rstrip().split()
    n = int(first_input[0])
    d = int(first_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = beautifulTriplets(d, arr)
    print (result)
