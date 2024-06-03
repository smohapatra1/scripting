# #   https://www.hackerrank.com/challenges/value-of-friendship/problem?isFullScreen=true

# You're researching friendships between groups of  new college students where each student is distinctly numbered from  to . At the beginning of the semester, no student knew any other student; instead, they met and formed individual friendships as the semester went on. The friendships between students are:

# Bidirectional. If student  is friends with student , then student  is also friends with student .
# Transitive. If student  is friends with student  and student  is friends with student , then student  is friends with student . In other words, two students are considered to be friends even if they are only indirectly linked through a network of mutual (i.e., directly connected) friends.
# The purpose of your research is to find the maximum total value of a group's friendships, denoted by . Each time a direct friendship forms between two students, you sum the number of friends that each of the  students has and add the sum to .

# You are given  queries, where each query is in the form of an unordered list of  distinct direct friendships between  students. For each query, find the maximum value of  among all possible orderings of formed friendships and print it on a new line.

# Input Format

# The first line contains an integer, , denoting the number of queries. The subsequent lines describe each query in the following format:

# The first line contains two space-separated integers describing the respective values of  (the number of students) and  (the number of distinct direct friendships).
# Each of the  subsequent lines contains two space-separated integers describing the respective values of  and  (where ) describing a friendship between student  and student .
# Constraints

# Output Format

# For each query, print the maximum value of  on a new line.

# Sample Input 0

# 1
# 5 4
# 1 2
# 3 2
# 4 2
# 4 3
# Sample Output 0

# 32
# Explanation 0

# image

# The value of  is maximal if the students form the  direct friendships in the following order:

# Students  and  become friends:
# image

# We then sum the number of friends that each student has to get .

# Students  and  become friends:
# image

# We then sum the number of friends that each student has to get .

# Students  and  become friends:
# image

# We then sum the number of friends that each student has to get .

# Students  and  become friends:
# image

# We then sum the number of friends that each student has to get .

# When we add the sums from each step, we get . We then print  on a new line.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'valueOfFriendsship' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY friendships
#
parent={}
no_of_friends={}

def findparent(x):
    if parent[x] == x:
        return x
    parent[x] = findparent(parent[x])
    return parent[x]

def value (n):
    t1=n*(n+1)*(2*n+1)
    t1/=6
    t2=n*(n+1)
    t2/=2
    return t1-t2

def valueOfFriendsship(n, friendships):
    # Write your code here
    total, current, ans =0,0,0
    for i in range(1,n+1):
        parent[i] = i
        no_of_friends[i] = 1
    for i in range(m):
        u,v=friendships[i][0],friendships[i][1]
        pu,pv = findparent(u),findparent(v)
        if pu != pv:
                parent[pv] = pu
                no_of_friends[pu] += no_of_friends[pv]              
    p=[]
    for i in range(1,n+1):
        if(parent[i] == i):
            p.append(no_of_friends[i])
    p.sort(reverse=True)
    for i in range(len(p)):
        current+=(p[i]-1)
        ans +=value(p[i])+total*(p[i]-1)
        total+=(p[i] * (p[i]-1))
    ans+=((m-current)*total)
    return int(ans) 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        friendships = []

        for _ in range(m):
            friendships.append(list(map(int, input().rstrip().split())))

        result = valueOfFriendsship(n, friendships)

        fptr.write(str(result) + '\n')

    fptr.close()
