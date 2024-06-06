# #   https://www.hackerrank.com/challenges/episode-recording/problem?isFullScreen=true

# Dave is a die-hard fan of a show called "HackerRank", in which a young programmer uses her problem-solving abilities to solve crimes. He splurged on a Digital Video Recorder (DVR) so that he can record HackerRank episodes and watch them later. Luckily, Dave managed to get his hands on schedules for all the episodes in each upcoming season.

# Each season has  episodes numbered from  to . Each episode airs twice; the first time it's called "live", and the second time it's called "repeat". So, for each episode, we have  integers,  and  for the live airing and  and  for the repeat airing, where  is episode's start time and and  is its end time. All times are given as integers representing the number of minutes passed since the start of the season.

# Episodes broadcast on multiple channels, so some of the air times overlap and the episodes may not broadcast sequentially. It's possible that both the live and repeat broadcasts of some episode  are held before episode , even though . In addition, live and repeat broadcasts of the same episode may differ in length due to the number of advertisements during the broadcast.

# Dave only has one TV with a DVR attached to it, and the DVR is capable of recording one episode at a time. For each episode in a season, Dave first decides whether or not he will record it. If he decides to record it, he will either record it during  or . Dave will only ever record one of the two airings of an episode, and he always records full episodes. This means that once he starts recording an episode, he will always record it until the end (i.e., he never records partial episodes).

# Dave realizes that it might not be possible for him to record all episodes successfully, so instead of focusing on recording all episodes of HackerRank (which may be impossible), he decides to record all consecutively airing episodes whose episode number occurs in some inclusive  interval such that  (i.e., the number of consecutive episodes recorded) is as large as possible.

# Given the programming schedule for each season, find  and  episode numbers for largest range of consecutive episodes Dave can record during that season and print these respective values as two space-separated integers on a new line. If two or more such intervals exist, choose the one having the smallest  value.

# Input Format

# The first line contains a single positive integer, , denoting number of seasons of HackerRank.
# The subsequent lines describe each of the  seasons in the following format:

# The first line contains an integer, , denoting the number of episodes in the season.
# Each line  of the  subsequent line contains four space-separated integers describing the respective values of , , , and .
# Constraints

# Output Format

# On a new line for each season, print two space-separated integers denoting the respective  and  (inclusive) values for the maximum possible range of consecutive episodes Dave can record such that  is as large as possible. If more than one such interval exists, choose the interval having the smallest .

# Sample Input

# 3
# 3
# 10 20 30 40
# 20 35 21 35
# 14 30 35 50
# 1
# 10 20 30 40
# 3
# 11 19 31 39
# 12 38 13 37
# 10 20 30 40
# Sample Output

# 1 2
# 1 1
# 1 1
# Explanation

# For the first season, Dave records the live airing of episode  and the repeat airing of episode . Note that it is not possible to record episodes ,  and  simultaneously.

# For the second season, there is only one episode so Dave records from episode  to episode  and we print 1 1 on a new line.

# For the third season, Dave must choose to record either episode  or episode  (episode  starts while episode  is still airing and ends after episode  starts); he cannot record both, because he only wants to record consecutive episodes. Thus, we pick the episode with the smallest  value, which is episode , and print 1 1 as we are only recording episode .



#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'episodeRecording' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY episodes as parameter.
#

#True if two intervals interesects
def has_intersection(I1,I2):
    if I1[0] >= I2[0] and I1[0] <= I2[1]: return True
    if I1[1] >= I2[0] and I1[1] <= I2[1]: return True
    if I2[0] >= I1[0] and I2[0] <= I1[1]: return True
    if I2[1] >= I1[0] and I2[1] <= I1[1]: return True
    return False

#Given the SAT Graph, return the longest interval with a dual-complete graph 
def max_range(G,GT):
    size = len(G)/4
    maxRange = [0,1]
    maxSize = 1

    a = 0
    b = 2

    while b <= size:
        SCC = []
        SCC = get_strong_connected_components(G,GT, a*4, b*4)
        newSize = b-a
        if is_satisfiable(SCC):
            if newSize > maxSize:
                maxRange = [a,b]
                maxSize = newSize
            b+=1
        else:
            if newSize == maxSize + 1:
                b+=1
            a+=1

    return maxRange

#Get the components only considering vertices between a (inclusive) and b (exclusive) indices
def get_strong_connected_components(G, GT, a, b):
    SCC = []
    numVertices = b-a
    compQueue = []
    Visited = [0 for c1 in range(numVertices)]
    for c1 in range(a,b):
        build_queue(G, a, b, compQueue, Visited, c1)
    while len(compQueue) > 0:
        i = compQueue.pop(-1)
        C = []
        build_component(GT, a, b, Visited, C, i)
        if len(C)>0: SCC.append(C)
    return SCC

def build_queue(G,a,b,compQueue, Visited, i):
    if Visited[i-a] == 1: return
    Visited[i-a] += 1

    for j in G[i]:
        if j>=a and j<b:
            build_queue(G, a, b, compQueue, Visited, j)
    compQueue.append(i)
    return

def build_component(GT, a, b, Visited, C, i):
    if Visited[i-a] == 2: return
    Visited[i-a] += 1
    for j in GT[i]:
        if j>=a and j<b:
            build_component(GT, a, b, Visited, C, j)
    C.append(i)
    return

    #returns False if for some a, a and not a are in the same component
def is_satisfiable(SCC):
    for C in SCC:
        C.sort()
        for c1 in range(len(C)-1):
            if C[c1+1]-C[c1] == 1 and C[c1]%2==0: return False
    return True

def build_digraph(S):
    size = len(S)*4
    G = []
    GT = []
    for c1 in range(size):
        G.append([])
        GT.append([])

    for c1 in range(len(S)):
        i = c1*4
        G[i+1].append(i+2)
        GT[i+2].append(i+1)
        G[i+3].append(i)
        GT[i].append(i+3)

    for c1 in range(len(S)):
        for c2 in range(2):
            i = c2*2
            tr1 = [S[c1][i],S[c1][i+1]]
            for c3 in range(c1, len(S)):
                for c4 in range(2):
                    if c1==c3 and c2==c4: continue
                    j = c4*2
                    tr2 = [S[c3][j],S[c3][j+1]]
                    if has_intersection(tr1,tr2):
                        k = c1*4
                        l = c3*4
                        G[k+i].append(l+j+1)
                        GT[l+j+1].append(k+i)
                        if c1!=c3:
                            G[l+j].append(k+i+1)
                            GT[k+i+1].append(l+j)

    return [G,GT]

    #main
q = int(input())
for c1 in range(q):
    n = int(input())
    S = []
    for c2 in range(n):
        s = input().split(' ')
        for c3 in range(len(s)):
            s[c3] = int(s[c3])
        S.append(s)
    G,GT = build_digraph(S)
    maxRange = max_range(G,GT)
    print(f'{maxRange[0]+1} {maxRange[1]}')
    

# def episodeRecording(episodes):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     q = int(input().strip())

#     for q_itr in range(q):
#         n = int(input().strip())

#         episodes = []

#         for _ in range(n):
#             episodes.append(list(map(int, input().rstrip().split())))

#         result = episodeRecording(episodes)

#         fptr.write(' '.join(map(str, result)))
#         fptr.write('\n')

#     fptr.close()
