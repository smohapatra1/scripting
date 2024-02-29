# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-dynamic-array/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-two
# Declare a 2-dimensional array, , of  empty arrays. All arrays are zero indexed.
# Declare an integer, , and initialize it to .

# There are  types of queries, given as an array of strings for you to parse:

# Query: 1 x y
# Let .
# Append the integer  to .
# Query: 2 x y
# Let .
# Assign the value  to .
# Store the new value of  to an answers array.
# Note:  is the bitwise XOR operation, which corresponds to the ^ operator in most languages. Learn more about it on Wikipedia.  is the modulo operator.
# Finally, size(arr[idx]) is the number of elements in arr[idx]

# Function Description

# Complete the dynamicArray function below.

# dynamicArray has the following parameters:
# - int n: the number of empty arrays to initialize in 
# - string queries[q]: query strings that contain 3 space-separated integers

# Returns

# int[]: the results of each type 2 query in the order they are presented
# Input Format

# The first line contains two space-separated integers, , the size of  to create, and , the number of queries, respectively.
# Each of the  subsequent lines contains a query string, .

# Constraints

# It is guaranteed that query type  will never query an empty array or index.
# Sample Input

# 2 5
# 1 0 5
# 1 1 7
# 1 0 3
# 2 1 0
# 2 1 1
# Sample Output

# 7
# 3
# Explanation

# Initial Values:


#  = [ ]
#  = [ ]

# Query 0: Append  to .

#  = [5]
#  = [ ]

# Query 1: Append  to .
#  = [5]
#  = [7]

# Query 2: Append  to .

#  = [5, 3]
#  = [7]

# Query 3: Assign the value at index  of  to , print .

#  = [5, 3]
#  = [7]

# 7
# Query 4: Assign the value at index  of  to , print .

#  = [5, 3]
#  = [7]

# 3


def dynamicArray(n, queries):
    last_answer=0
    arr=[[] for _ in range(n)]
    results=[]
    for q, x, y in queries:
        if q == 1:
            idx=(x ^ last_answer) % n 
            arr[idx].append(y)
        elif q == 2:
            idx=(x ^ last_answer) % n 
            last_answer = arr[idx][y% len(arr[idx])]
            results.append(last_answer)
    return results

if __name__ == "__main__":
    a=input().strip().split()
    n=int(a[0])
    q=int(a[1])
    queries=[]
    for i in range(q):
        queries.append(list(map(int, input().strip().split())))
    result = dynamicArray(n, queries)
    print (result)