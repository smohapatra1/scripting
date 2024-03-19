# #   https://www.hackerrank.com/challenges/frog-in-maze/problem?isFullScreen=true

# Alef the Frog is in an  two-dimensional maze represented as a table. The maze has the following characteristics:

# Each cell can be free or can contain an obstacle, an exit, or a mine.
# Any two cells in the table considered adjacent if they share a side.
# The maze is surrounded by a solid wall made of obstacles.
# Some pairs of free cells are connected by a bidirectional tunnel.
# image

# When Alef is in any cell, he can randomly and with equal probability choose to move into one of the adjacent cells that don't contain an obstacle in it. If this cell contains a mine, the mine explodes and Alef dies. If this cell contains an exit, then Alef escapes the maze.

# When Alef lands on a cell with an entrance to a tunnel, he is immediately transported through the tunnel and is thrown into the cell at the other end of the tunnel. Thereafter, he won't fall again, and will now randomly move to one of the adjacent cells again. (He could possibly fall in the same tunnel later.)

# It's possible for Alef to get stuck in the maze in the case when the cell in which he was thrown into from a tunnel is surrounded by obstacles on all sides.

# Your task is to write a program which calculates and prints a probability that Alef escapes the maze.

# Input Format

# The first line contains three space-separated integers ,  and  denoting the dimensions of the maze and the number of bidirectional tunnels.

# The next  lines describe the maze. The 'th line contains a string of length  denoting the 'th row of the maze. The meaning of each character is as follows:

# # denotes an obstacle.
# A denotes a free cell where Alef is initially in.
# * denotes a cell with a mine.
# % denotes a cell with an exit.
# O denotes a free cell (which may contain an entrance to a tunnel).
# The next  lines describe the tunnels. The 'th line contains four space-separated integers , , , . Here,  and  denote the coordinates of both entrances of the tunnel.  denotes the row and column number, respectively.

# Constraints

#  and  are distinct.
# A appears exactly once.
# Each free cell contains at most one entrance to a tunnel.
# If a cell contains an entrance to a tunnel, then it doesn't contain an obstacle, mine or exit, and Alef doesn't initially stand in it.
# Tunnels don't connect adjacent cells.
# Output Format

# Print one real number denoting the probability that Alef escapes the maze. Your answer will be considered to be correct if its (absolute) difference from the true answer is not greater than .

# Sample Input 0

# 3 6 1
# ###*OO
# O#OA%O
# ###*OO
# 2 3 2 1
# Sample Output 0

# 0.25
# Explanation 0

# The following depicts this sample case:

# image

# In this case, Alef will randomly choose one of four adjacent cells. If he goes up or down, he will explode and die. If he goes right, he will escape. If he goes left, he will go through a tunnel and get stuck in cell . So the probability of Alef escaping is .


#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    k = int(first_multiple_input[2])

    board = [list(input()) for _ in range(n)]
    t_exit = dict()
    
    for kk in range(k):
        second_multiple_input = input().rstrip().split()
        i1 = int(second_multiple_input[0]) - 1
        j1 = int(second_multiple_input[1]) - 1
        i2 = int(second_multiple_input[2]) - 1
        j2 = int(second_multiple_input[3]) - 1
        t_exit[(i1, j1)] = (i2, j2)
        t_exit[(i2, j2)] = (i1, j1)

    states = [(-1, -1)]  # Death state.
    state2idx = dict()
    v = [0.0]  # State values, i.e. probability.
    s_init = -1
    transitions = [[(0, 1.0)]]  # Self loop when dead.
    
    for i1 in range(n):
        for j1 in range(m):
            x = board[i1][j1]
            if x in ["A", "%", "O"]:
                state2idx[(i1, j1)] = len(states)
                states.append((i1, j1))
            elif x in ["#", "*"]:
                state2idx[(i1, j1)] = 0       
            else:
                assert False, x
    
    for i1 in range(n):
        for j1 in range(m):
            x = board[i1][j1]
            state_idx = state2idx[(i1, j1)]
            if x in ["A", "%", "O"]:
                if x == "A":
                    s_init = state_idx
                    v.append(0.0)
                elif x == "%":
                    v.append(1.0)
                    transitions.append([(state_idx, 1.0)])  # Self loop when exit.
                elif x == "O":
                    v.append(0.0)
                else:
                    assert False, x
                if x in ["A", "O"]:
                    i2, j2 = t_exit[(i1, j1)] if (i1, j1) in t_exit else (i1, j1)
                    succs = []
                    deaths = 0
                    for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        i3, j3 = i2 + a, j2 + b
                        if (0 <= i3 < n) and (0 <= j3 < m):
                            y = board[i3][j3]
                            if y in ["A", "%", "O"]:
                                succs.append((i3, j3))
                            elif y == "*":
                                deaths += 1
                    if len(succs) == 0:
                        transitions.append([(0, 1.0)])
                    else:
                        t = [(state2idx[s], 1 / (len(succs) + deaths)) for s in succs]
                        if deaths > 0:
                            t.append((0, deaths / (len(succs) + deaths)))
                        transitions.append(t)
          
    while True:
        v_old = v.copy()
        for state in range(len(states)):
            x = 0.0
            for succ, prob in transitions[state]:
                x += v[succ] * prob
            v[state] = x
        keep_going = False
        for state in range(len(states)):
            if abs(v[state] - v_old[state]) > 1e-10:
                keep_going = True
                break
        if not keep_going:
            break

    print(v[s_init])