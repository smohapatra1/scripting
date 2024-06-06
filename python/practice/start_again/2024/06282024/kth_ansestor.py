# #   https://www.hackerrank.com/challenges/kth-ancestor/problem?isFullScreen=true

# A tree of  nodes is an un-directed connected graph having  edges. Let us denote  as the root node. If  is a node such that it is at a distance of  from , and  is a node such that it is at at distance of  from  and  is connected to , then we call  as the parent of .

# Similarly, if  is at a distance of  from  and  is at a distance of  from  and there is a path of length  from  to , then we call  as the th parent of .

# Susan likes to play with graphs and Tree data structure is one of her favorites. She has designed a problem and wants to know if anyone can solve it. Sometimes she adds or removes a leaf node. Your task is to figure out the th parent of a node at any instant.

# Input Format

# The first line contain an integer  denoting the number of test cases.  test cases follow. First line of each test case contains an integer , the number of nodes in the tree.  lines follows each containing two integers  and  separated by a single space denoting  as the parent of . If  is , then X is the root node of the tree. ( is for namesake and is not in the tree).
# The next line contains an integer , the number of queries.
#  lines follow each containing a query.

#    :  is added as a new leaf node whose parent is  .  is not in the tree while  is in.
#   : This tells that leaf node  is removed from the tree.  is a leaf in the tree.
#    : In this query output the th parent of  .  is a node in the tree.
# Note

# Each node index is any number between 1 and 105 i.e., a tree with a single node can have its root indexed as 105
# Constraints







# Output Format

# For each query of type , output the th parent of . If th parent doesn't exist, output  and if the node doesn't exist, output .

# Sample Input

# 2
# 7
# 2 0
# 5 2
# 3 5
# 7 5
# 9 8
# 8 2
# 6 8
# 10
# 0 5 15
# 2 15 2
# 1 3
# 0 15 20
# 0 20 13
# 2 13 4
# 2 13 3
# 2 6 10
# 2 11 1
# 2 9 1
# 1
# 10000 0
# 3
# 0 10000 4
# 1 4
# 2 4 1
# Sample Output

# 2
# 2
# 5
# 0
# 0
# 8
# 0
# Explanation

# There are 2 test cases. The first test case has 7 nodes with 2 as its root. There are 10 queries

# 0 5 15 -> 15 is added as a leaf node to 5.
# 2 15 2 -> 2nd parent of 15 is 15->5->2 is 2.
# 1 3 -> leaf node 3 is removed from the tree.
# 0 15 20 -> 20 is added as a leaf node to 15.
# 0 20 13 -> 13 is added as a leaf node to 20.
# 2 13 4 -> 4th parent of 13 is 2.
# 2 13 3 -> 3rd parent of 13 is 5.
# 2 6 10 -> there is no 10th parent of 6 and hence 0.
# 2 11 1 -> 11 is not a node in the tree, hence 0.
# 2 9 1 -> 9's parent is 8.
# the second testcase has a tree with only 1 node (10000).

# 0 10000 4 -> 4 is added as a leaf node to 10000.
# 1 4 -> 4 is removed.
# 2 4 1 -> as 4 is already removed, answer is 0.
# Language
# Python 3
# More
# 90919293949596979899100101102103104105106107108109110111112113114115116
#                         a = 0
#                         break
#                     node = G[node.ancestors[log]]
#                     a = node.i
#                     k -= 2 ** log
#             print(a)
# Line: 116 Col: 21

# Test against custom input
# Problem Solving
# You have earned 90.00 points!
# 276/563 challenges solved.
# 49%
# Congratulations
# You solved this challenge. Would you like to challenge your friends?Share on FacebookShare on TwitterShare on LinkedIn

# Test case 0

# Test case 1

# Test case 2

# Test case 3

# Test case 4

# Test case 5

# Test case 6

# Test case 7

# Test case 8

# Test case 9

# Test case 10

# Test case 11

# Test case 12

# Test case 13

# Test case 14
# Compiler Message
# Success
# Input (stdin)
# 2
# 7
# 2 0
# 5 2
# 3 5
# 7 5
# 9 7
# 8 2
# 6 8
# 10
# 0 5 15
# 2 15 2
# 1 3
# 0 15 20
# 0 20 13
# 2 13 4
# 2 13 3
# 2 6 10
# 2 11 1
# 2 9 1{-truncated-}
# Expected Output
# 2
# 2
# 5
# 0
# 0
# 7
# 0
# BlogScoringEnvironmentFAQAbout UsSupportCareersTerms Of ServicePrivacy Policy

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import math
from typing import Deque
sys.setrecursionlimit(1000000)

class Node:
    def __init__(self, i, depth, children, ancestors):
        self.i = i
        self.depth = depth
        self.children = set(children)
        self.ancestors = list(ancestors)

def print_graph(G):
    for X in G:
        node = G[X]
        print(node)
    print()
    
def dfs(G, u):
    node = G[u]
    if node.ancestors[0] != 0:
        log = math.floor(math.log(node.depth, 2))
        for i in range(1, log + 1):
            ancestor = G[node.ancestors[i - 1]]
            if not len(ancestor.ancestors) > i - 1:
                break
            node.ancestors.append(ancestor.ancestors[i - 1])
    for v in node.children:
        child = G[v]
        child.depth = node.depth + 1
        dfs(G, v)

def dfs_stack(G, u):
    stack = Deque([u])
    while stack:
        u = stack.pop()
        node = G[u]
        if node.ancestors[0] != 0:
            log = math.floor(math.log(node.depth, 2))
            for i in range(1, log + 1):
                ancestor = G[node.ancestors[i - 1]]
                if not len(ancestor.ancestors) > i - 1:
                    break
                node.ancestors.append(ancestor.ancestors[i - 1])
        for v in node.children:
            child = G[v]
            child.depth = node.depth + 1
            stack.append(v)

T = int(sys.stdin.readline())
for _ in range(T):
    P = int(sys.stdin.readline())
    S = set()
    #G = {}
    G = [None] * 100001
    for _ in range(P):
        X, Y = list(map(int, sys.stdin.readline().strip().split(' ')))
        S.add(X)
        if Y == 0:
            G[X] = Node(X, 0, [], [0])
        else:
            G[X] = Node(X, 0, [], [Y])
    
    root = None
    #for X in G:
    for X in S:
        node = G[X]
        if node.ancestors[0] != 0:
            parent = G[node.ancestors[0]]
            parent.children.add(X)
        else:
            root = X
    
    #print_graph(G)
    #G[0] = Node(0, 0, [], [0])
    dfs_stack(G, root)
    #print_graph(G)
    
    Q = int(sys.stdin.readline())
    for _ in range(Q):
        q = list(map(int, sys.stdin.readline().strip().split(' ')))
        if q[0] == 0:
            Y, X = q[1:]
            parent = G[Y]
            #parent.children.add(X)
            node = Node(X, parent.depth + 1, [], [Y])
            G[X] = node
            dfs_stack(G, X)
            #print_graph(G)
        elif q[0] == 1:
            X = q[1]
            node = G[X]
            #if node.ancestors[0] != 0:
            #    parent = G[node.ancestors[0]]
            #    parent.children.remove(X)
            G[X] = None
            #G.pop(X)
            #print_graph(G)
        elif q[0] == 2:
            X, K = q[1:]
            a = 0
            #if X in G:
            if G[X] is not None:
                node = G[X]
                k = K
                while k > 0:
                    log = math.floor(math.log(k, 2))
                    if not len(node.ancestors) > log or not node.ancestors[log] != 0:
                        a = 0
                        break
                    node = G[node.ancestors[log]]
                    a = node.i
                    k -= 2 ** log
            print(a)
            