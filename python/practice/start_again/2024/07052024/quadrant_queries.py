#   https://www.hackerrank.com/challenges/quadrant-queries/problem?isFullScreen=true

# There are  points on a plane. Each point  is described by , where . There are three types of queries needed: 

# X i j Reflect all points in the inclusive range between points  and  along the -axis.
# Y i j Reflect all points in the inclusive range between points  and  along the -axis.
# C i j Count the number of points in the inclusive range between points  and  in each of the  quadrants. Then print a single line of four space-separated integers describing the respective numbers of points in the first, second, third, and fourth quadrants in that order.
# As a reminder, the four quadrants of a graph are labeled as follows:


# Given a set of  points and  queries, perform each query in order. For example, given points  and . Initially the points are in quadrants  and . The first query says to reflect points with indices from  to  along the -axis. After the query,  and quadrants are  and . The next query prints the number of points in each quadrant: 0 1 0 1. The third query says to reflect the point with index  to  along the -axis, so now . The points now lie in quadrants  and , so the fourth query output is 0 1 1 0.

# Note: Points may sometimes share the same coordinates.

# Function Description

# Complete the quadrants function in the editor below. It should print the results of each C type query on a new line.

# quadrants has the following parameters:
# - p[p[1]...p[n]]: a 2-dimensional array of integers where each element  contains two integers  and 
# - queries[queries[1]...queries[n]: an array of strings

# Input Format

# The first line contains a single integer, , that denotes the number of points.
# Each line  of the  subsequent lines contains two space-separated integers that describe the respective  and  values for point  .
# The next line contains a single integer, , that denotes the number of queries.
# Each of the  subsequent lines contains three space-separated values that describe a query in one of the three forms defined above.

# Constraints

# No point lies on the  or  axes.
# In all queries, .
# Output Format

# For each query of type C i j, print four space-separated integers that describe the number of points having indices in the inclusive range between  and  in the first, second, third, and fourth graph quadrants in that order.

# Sample Input

# 4
# 1 1
# -1 1
# -1 -1
# 1 -1
# 5
# C 1 4
# X 2 4
# C 3 4
# Y 1 2
# C 1 3
# Sample Output

# 1 1 1 1
# 1 1 0 0
# 0 2 0 1
# Explanation

# Initially,  so there is one point in each of the four quadrants. The first query results in printing 1 1 1 1.

# The second query, X 2 4, reflects the points in the inclusive range between indices  and  along the -axis. Now .

# The query C 3 4 requires that the number of points considering  through  be printed: 1 1 0 0

# The third query, Y 1 2 requires reflection of  along the -axis. Now .

# The last query, C 1 3 requires that the number of points considering  through  be printed: 0 2 0 1





#!/bin/python3

import math
import os
import random
import re
import sys
import bisect
from math import sqrt
import optparse
import sys
from random import randint as rand

_Rx = [3, 2, 1, 0]
_Ry = [1, 0, 3, 2]

def create_test(N, Q, fp):
    r = [(rand(-2, 2), rand(-2, 2)) for i in range(N)]
    print(N, file = fp)
    for ri in r:
        print('%d %d' % ri, file = fp)
    ops = [ "X", "Y", "C" ]
    queries = [(ops[rand(0, 2)], rand(1, N), rand(1, N)) for q in range(Q)]
    print(Q, file = fp)
    for op, i, j in queries:
        if i > j: 
            i, j = j, i
        print('%1s %d %d' % (op, i, j), file = fp)
    return [r, queries]
    
def quadrant(x, y):
    '''
    Return the quadrant the point r is in.
    '''
    if x > 0:
        if y > 0: return 0
        else: return 3
    else:
        if y > 0: return 1
        else: return 2
    
def getInput(f, shift = -1):
    '''
    The first line contains N, the number of points. N lines follow.
    The ith line contains xi and yi separated by a space.  The next line
    contains Q the number of queries. The next Q lines contain one query
    each, of one of the above forms.  All indices are 1 indexed.

    Return the points r and the queries q, in [r, q]
    '''
    l = f.readline().strip()
    n = int(l)
    r = []
    for i in range(n):
        l = f.readline().strip()
        x, y = l.split()
        r.append([int(x), int(y)])
    l = f.readline().strip()
    Q = int(l)
    queries = []
    for k in range(Q):
        l = f.readline().strip()
        op, i, j = l.split()
        queries.append((op, int(i) + shift, int(j) + shift))
    return [r, queries]

class QuadrantBook:
    '''
    A data structure to facilitate the processing of quadrant queries.
    '''
    def __init__(self, r, factor = 32):
        N = len(r)
        self.blocksize = int(sqrt(factor * N))
        nblocks = (N - 1) // self.blocksize + 1
        # self.inq[b][q] is the list of points in the quadrant q with indices
        # between b L and (b+1)L, where L is the blocksize.
        self.inq = [[[] for q in range(4) ] for b in range(nblocks)]
        for i, ri in enumerate(r):
            b = self.getBlock(i)
            q = quadrant(ri[0], ri[1])
            self.inq[b][q].append(i)

    def countInQuadrants( self, i, j):
        '''
        Count the number of points in each quadrant with indices between i and j,
        inclusive.
        '''
        bi = self.getBlock(i)
        bj = self.getBlock(j)
        cq = [0] * 4
        if bi == bj:
            for q, idx in enumerate(self.inq[bi]):
                ki, kj = getIndex(idx, i, j)
                cq[q] = kj - ki
            return cq
        else:
            for q in range(4):
                ni = self.inq[bi][q]
                nj = self.inq[bj][q]
                ki = bisect.bisect_left(ni, i)
                kj = bisect.bisect_right(nj, j)
                cq[q] = len(ni) - ki 
                for nb in self.inq[bi + 1: bj]:
                    cq[q] += len(nb[q])
                cq[q] += kj
            return cq

    def reflect( self, i, j, axis):
        '''
        Update the list of points in each quadrant after reflection along the
        given axis.
        '''
        if axis == "X":
            R = _Rx
            W = [(0, 3), (1, 2)]
        else:
            R = _Ry
            W = [(0, 1), (2, 3)]    
        bi = self.getBlock( i)
        bj = self.getBlock( j)
        if bi == bj:
            self.reflectInBlock( i, j, bi, R)
        else:
            ni = self.inq[bi]
            kiq = [bisect.bisect_left(idx, i) for idx in ni]
            rfxi = [ni[q][ki:] for q, ki in enumerate(kiq)]
            for q, ki in enumerate(kiq):
                ni[q] = ni[q][:ki] + rfxi[R[q]]   
            nj = self.inq[bj]
            kjq = [bisect.bisect_right( idx, j) for idx in nj]
            rfxj = [nj[q][:kj] for q, kj in enumerate(kjq)]
            for q, kj in enumerate( kjq):
                nj[q] = rfxj[R[q]] + nj[q][kj:]    
            for nb in self.inq[bi + 1: bj]:
                for w1, w2 in W:
                    nb[w1], nb[w2] = nb[w2], nb[w1]
          
    def getBlock( self, i ):
        '''
        Get the block index for point i.
        '''
        return i // self.blocksize


    def reflectInBlock(self, i, j, b, R):
        '''
        Update the list of points in each quadrant after reflection along the
        given axis, assuming that i and j are in the same block b.
        '''
        nb = self.inq[b]
        kij = [getIndex( idx, i, j) for idx in nb]
        rf = [nb[q][ki: kj] for q, (ki, kj) in enumerate(kij)]
        for q, (ki, kj) in enumerate(kij):
            nb[q] = nb[q][:ki] + rf[R[q]] + nb[q][kj:]

def getIndex( lst, i, j):
    '''
    In the sorted list, find ki such that lst[ki-1]<i<=lst[ki], and kj such
    that lst[kj]<=j<lst[kj+1]. If i<lst[0], ki=0; if j>lst[-1], kj=len(lst).
    This convention splices the list at the right places.

    @param i<=j
    '''
    ki = bisect.bisect_left(lst, i)
    kj = bisect.bisect_right(lst, j, ki)
    return [ki, kj]

def processQueries(r, queries, factor = 32):
    qbook = QuadrantBook(r, factor)
    for op, i, j in queries:
        if op.upper() == 'C':
            cq = qbook.countInQuadrants(i, j)
            print('%d %d %d %d' % tuple(cq), file = sys.stdout)
        elif op.upper() in ['X', 'Y']:
            qbook.reflect( i, j, op)


if __name__ == '__main__':
    usage = '%prog'
    opt = optparse.OptionParser(usage)
    opt.add_option('-N', type = 'int', default = 100)
    opt.add_option('-Q', type = 'int', default = 10)
    opt.add_option('-c', '--create', action = 'store_true', default = False, help = 'Create test case instead of running the query.')
    opt.add_option('-i', '--input', type='string', default = None, help = 'Input file.')
    opt.add_option('-b', '--block-factor', type = 'float', default = 32., help = 'Use sqrt(b * N) as the block size.')
    opts, args = opt.parse_args()
    if opts.create:
        r, queries = create_test(opts.N, opts.Q, sys.stdout)
    else:
        r, queries = getInput(opts.input and open(opts.input, 'r') or sys.stdin)
        processQueries(r, queries, opts.block_factor)
        
#
# Complete the 'quadrants' function below.
#
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY p
#  2. STRING_ARRAY queries
#

# def quadrants(p, queries):
#     # Write your code here

# if __name__ == '__main__':
#     n = int(input().strip())

#     p = []

#     for _ in range(n):
#         p.append(list(map(int, input().rstrip().split())))

#     q = int(input().strip())

#     queries = []

#     for _ in range(q):
#         queries_item = input()
#         queries.append(queries_item)

#     quadrants(p, queries)

