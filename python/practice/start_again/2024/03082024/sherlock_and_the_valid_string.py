# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-sherlock-and-valid-string/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-three

# Sherlock considers a string to be valid if all characters of the string appear the same number of times. It is also valid if he can remove just  character at  index in the string, and the remaining characters will occur the same number of times. Given a string , determine if it is valid. If so, return YES, otherwise return NO.

# Example

# This is a valid string because frequencies are .


# This is a valid string because we can remove one  and have  of each character in the remaining string.


# This string is not valid as we can only remove  occurrence of . That leaves character frequencies of .

# Function Description

# Complete the isValid function in the editor below.

# isValid has the following parameter(s):

# string s: a string
# Returns

# string: either YES or NO
# Input Format

# A single string .

# Constraints

# Each character 
# Sample Input

# aabbcd
# Sample Output

# NO
# Explanation

#  is the minimum number of removals required to make it a valid string. It can be done in following two ways:

# Remove c and d to get aabb.
# Or remove a and b to get abcd.
from collections import Counter



def isValid(s):
    # Write your code here
    freq_counter=Counter(s)
    freq=Counter(freq_counter.values())
    if len(freq) == 1:
        return 'YES'
    elif len(freq) == 2:
        (k1, v1 ), (k2, v2) = freq.items()
        if v1== 1 and (k1-1 == k2 or k1==1) or v2==1 and (k2 -1 ==k1 or k2 ==1):
            return 'YES'
    return 'NO'
    

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = isValid(s)
    print (result)

    # fptr.write(result + '\n')

    # fptr.close()