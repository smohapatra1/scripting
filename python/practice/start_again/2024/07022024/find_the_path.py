# #   https://www.hackerrank.com/challenges/shortest-path/problem?isFullScreen=true

# You are given a table, , with  rows and  columns. The top-left corner of the table has coordinates , and the bottom-right corner has coordinates . The  cell contains integer .

# A path in the table is a sequence of cells  such that for each , cell  and cell  share a side.

# The weight of the path  is defined by  where  is the weight of the cell .

# You must answer  queries. In each query, you are given the coordinates of two cells,  and . You must find and print the minimum possible weight of a path connecting them.

# Note: A cell can share sides with at most  other cells. A cell with coordinates  shares sides with , ,  and .

# Input Format

# The first line contains  space-separated integers,  (the number of rows in ) and  (the number of columns in ), respectively.
# Each of  subsequent lines contains  space-separated integers. The  integer in the  line denotes the value of .
# The next line contains a single integer, , denoting the number of queries.
# Each of the  subsequent lines describes a query in the form of  space-separated integers: , , , and , respectively.

# Constraints

# For each query:

# Output Format

# On a new line for each query, print a single integer denoting the minimum possible weight of a path between  and .

# Sample Input

# 3 5
# 0 0 0 0 0
# 1 9 9 9 1
# 0 0 0 0 0
# 3
# 0 0 2 4
# 0 3 2 3
# 1 1 1 3
# Sample Output

# 1
# 1
# 18
# Explanation

# The input table looks like this:

# Initial Table

# The first two queries are explained below:

# In the first query, we have to find the minimum possible weight of a path connecting  and . Here is one possible path: First Query Path

# The total weight of the path is .

# In the second query, we have to find the minimum possible weight of a path connecting  and . Here is one possible path: Second Query Path The total weight of the path is .


#!/bin/python3

import math
import os
import random
import re
import sys
from heapq import *

num_rows = 0
num_cols = 0
num_queries = 0
table = []
query_dict = {}
query_results = []
shortest_paths = []
visited = []


def read_input():
    global num_rows, num_cols, num_queries, table, query_dict, query_results, shortest_paths, visited
    
    num_rows, num_cols = map(int, input().split())
    for i in range(num_rows):
        row = []
        entry_list = input().split()
        for j in range(num_cols):
            row.append(int(entry_list[j]))
        table.append(row)

    shortest_paths = [ [ sys.maxsize for j in range(num_cols) ] for i in range(num_rows) ]
    visited = [ [ False for j in range(num_cols) ] for i in range(num_rows) ]  
    
    num_queries = int(input())
    for i in range(num_queries):
        query_results.append(sys.maxsize)
        query = list(map(int, input().split()))
        if query[1] > query[3]:
            query = (query[2], query[3], query[0], query[1])
        else:
            query = (query[0], query[1], query[2], query[3])
        
        if query not in query_dict:
            query_dict[query] = []
        query_dict[query].append(i)
    
    
def is_valid_square(row, col, left_bound, right_bound):
    return row >= 0 and row < num_rows and col >= left_bound and col <= right_bound

    
def process_single_square(start_row, start_col, left_bound, right_bound):
    global shortest_paths, visited
    
    for i in range(num_rows):
        for j in range(left_bound, right_bound + 1):
            shortest_paths[i][j] = sys.maxsize
            visited[i][j] = False  
    
    bfs_heap = []
    shortest_paths[start_row][start_col] = table[start_row][start_col]
    heappush(bfs_heap, (table[start_row][start_col], start_row, start_col))
    
    while bfs_heap:
        weight, row, col = heappop(bfs_heap)
        if visited[row][col]:
            continue         
            
        visited[row][col] = True
        
        if is_valid_square(row - 1, col, left_bound, right_bound) and not visited[row - 1][col] :
            if weight + table[row - 1][col] < shortest_paths[row - 1][col]:
                shortest_paths[row - 1][col] = weight + table[row - 1][col]
                heappush(bfs_heap, (weight + table[row - 1][col], row - 1, col))
        if is_valid_square(row + 1, col, left_bound, right_bound) and not visited[row + 1][col]:
            if weight + table[row + 1][col] < shortest_paths[row + 1][col]:
                shortest_paths[row + 1][col] = weight + table[row + 1][col]
                heappush(bfs_heap, (weight + table[row + 1][col], row + 1, col))
        if is_valid_square(row, col - 1, left_bound, right_bound) and not visited[row][col - 1]:
            if weight + table[row][col - 1] < shortest_paths[row][col - 1]:
                shortest_paths[row][col - 1] = weight + table[row][col - 1]
                heappush(bfs_heap, (weight + table[row][col - 1], row, col - 1))               
        if is_valid_square(row, col + 1, left_bound, right_bound) and not visited[row][col + 1]:
            if weight + table[row][col + 1] < shortest_paths[row][col + 1]:
                shortest_paths[row][col + 1] = weight + table[row][col + 1]
                heappush(bfs_heap, (weight + table[row][col + 1], row, col + 1))
                        

def process_only_one_column(start_row, col_index):
    shortest_paths = [ sys.maxsize for i in range(num_rows) ]
    shortest_paths[start_row] = table[start_row][col_index]
    
    weight = table[start_row][col_index]
    for i in reversed(range(0, start_row)):
        weight = weight + table[i][col_index]
        shortest_paths[i] = weight
    
    weight = table[start_row][col_index]
    for i in range(start_row + 1, num_rows):
        weight = weight + table[i][col_index]
        shortest_paths[i] = weight
        
    return shortest_paths
    
    
def process_queries_by_column(left_col, right_col, whole_queries):
    global query_results
        
    if not whole_queries:
        return

    if left_col  >= right_col:
        for query in whole_queries:
            query_indexes = whole_queries[query]
            paths = process_only_one_column(query[0], left_col)
            new_min = min(query_results[query_indexes[0]], paths[query[2]])
            for q_index in query_indexes:
                query_results[q_index] = new_min
        return
    
    paths = []
    middle_col = (left_col + right_col) // 2
    for i in range(num_rows):
        process_single_square(i, middle_col, left_col, right_col)
        for query in whole_queries:
            query_indexes = whole_queries[query]
            tmp_w = shortest_paths[query[0]][query[1]] + shortest_paths[query[2]][query[3]] - table[i][middle_col]
            if tmp_w < query_results[query_indexes[0]]:
                for q_index in query_indexes:
                    query_results[q_index] = tmp_w
    
    queries_on_left = {}
    queries_on_right = {}
    for query in whole_queries:
        query_indexes = whole_queries[query]
        if query[3] < middle_col:
            queries_on_left[query] = query_indexes
        if query[1] > middle_col:
            queries_on_right[query] = query_indexes
                            
    process_queries_by_column(left_col, middle_col - 1, queries_on_left)
    process_queries_by_column(middle_col + 1, right_col, queries_on_right)
        
        
def print_query_results():
    for q_result in query_results:
        print(q_result)
    
    
if __name__ == '__main__':
    read_input()
    process_queries_by_column(0, num_cols - 1, query_dict)
    print_query_results() 


# #
# # Complete the 'shortestPath' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts following parameters:
# #  1. 2D_INTEGER_ARRAY a
# #  2. 2D_INTEGER_ARRAY queries
# #

# def shortestPath(a, queries):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     m = int(first_multiple_input[1])

#     a = []

#     for _ in range(n):
#         a.append(list(map(int, input().rstrip().split())))

#     q = int(input().strip())

#     queries = []

#     for _ in range(q):
#         queries.append(list(map(int, input().rstrip().split())))

#     result = shortestPath(a, queries)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()

