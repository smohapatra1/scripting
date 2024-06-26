# #   https://www.hackerrank.com/challenges/insertionsort2/problem?isFullScreen=true

# In Insertion Sort Part 1, you inserted one element into an array at its correct sorted position. Using the same approach repeatedly, can you sort an entire array?

# Guideline: You already can place an element into a sorted array. How can you use that code to build up a sorted array, one element at a time? Note that in the first step, when you consider an array with just the first element, it is already sorted since there's nothing to compare it to.

# In this challenge, print the array after each iteration of the insertion sort, i.e., whenever the next element has been inserted at its correct position. Since the array composed of just the first element is already sorted, begin printing after placing the second element.

# Example.



# Working from left to right, we get the following output:

# 3 4 7 5 6 2 1
# 3 4 7 5 6 2 1
# 3 4 5 7 6 2 1
# 3 4 5 6 7 2 1
# 2 3 4 5 6 7 1
# 1 2 3 4 5 6 7
# Function Description

# Complete the insertionSort2 function in the editor below.

# insertionSort2 has the following parameter(s):

# int n: the length of 
# int arr[n]: an array of integers
# Prints

# At each iteration, print the array as space-separated integers on its own line.

# Input Format

# The first line contains an integer, , the size of .
# The next line contains  space-separated integers .

# Constraints



# Output Format

# Print the entire array on a new line at every iteration.

# Sample Input

# STDIN           Function
# -----           --------
# 6               n = 6
# 1 4 3 5 6 2     arr = [1, 4, 3, 5, 6, 2]
# Sample Output

# 1 4 3 5 6 2 
# 1 3 4 5 6 2 
# 1 3 4 5 6 2 
# 1 3 4 5 6 2 
# 1 2 3 4 5 6 
# Explanation

# Skip testing  against itself at position . It is sorted.
# Test position  against position : , no more to check, no change.
# Print 
# Test position  against positions  and :

# , new position may be . Keep checking.
# , so insert  at position  and move others to the right.
# Print 
# Test position  against positions  (as necessary): no change.
# Print 
# Test position  against positions : no change.
# Print 
# Test position  against positions , insert  at position  and move others to the right.
# Print 

def insertionSort2(n, arr):
    for i in range(1,n):
        while i-1 >=0:
            if arr[i] < arr[i-1]:
                temp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = temp
            else:
                break
        print (*arr)

if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = insertionSort2(n, arr)