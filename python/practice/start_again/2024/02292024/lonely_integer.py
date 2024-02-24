# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-lonely-integer/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one

# Given an array of integers, where all elements but one occur twice, find the unique element.

# Example

# The unique element is .

# Function Description

# Complete the lonelyinteger function in the editor below.

# lonelyinteger has the following parameter(s):

# int a[n]: an array of integers
# Returns

# int: the element that occurs only once
# Input Format

# The first line contains a single integer, , the number of integers in the array.
# The second line contains  space-separated integers that describe the values in .

# Constraints

# It is guaranteed that  is an odd number and that there is one unique element.
# , where .

def lonelyinteger(a):
    res=0
    for elm in arr:
        res ^=elm
    return res

if __name__ == "__main__":
    n=int(input().strip())
    arr=list(map(int, input().strip().split()))
    res=lonelyinteger(arr)
    print (res)