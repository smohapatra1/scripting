# https://www.hackerrank.com/challenges/mr-k-marsh/problem?isFullScreen=true
# # Mr K has a rectangular plot of land which may have marshes where fenceposts cannot be set. He wants you to find the perimeter of the largest rectangular fence that can be built on this land.

# For example, in the following  grid,  marks a marsh and  marks good land.

# ....
# ..x.
# ..x.
# x...
# If we number the rows and columns starting with , we see that there are two main areas that can be fenced:  and . The longest perimeter is .

# Function Description

# Complete the kMarsh function in the editor below. It should print either an integer or impossible.

# kMarsh has the following parameter(s):

# grid: an array of strings that represent the grid
# Input Format

# The first line contains two space-separated integers  and , the grid rows and columns.
# Each of the next  lines contains  characters each describing the state of the land. 'x' (ascii value: 120) if it is a marsh and '.' ( ascii value:46) otherwise.

# Constraints


# Output Format

# Output contains a single integer - the largest perimeter. If the rectangular fence cannot be built, print impossible.

# Sample Input 0

# 4 5
# .....
# .x.x.
# .....
# .....
# Sample Output 0

# 14
# Explanation 0

# The fence can be put up around the entire field. The perimeter is .

# Sample Input 1

# 2 2
# .x
# x.
# Sample Output 1

# impossible
# Explanation 1

# We need a minimum of 4 points to place the 4 corners of the fence. Hence, impossible.

# Sample Input 2

# 2 5
# .....
# xxxx.
# Sample Output 2

# impossible 


def kMarsh(grid):
    # Write your code here
    max_dists_vert = {k:{} for k in range(m)}
    max_dists_horiz = {k:{} for k in range(m)}

    for i in range(m):
        max_dists_horiz[i][0] = 1*(grid[i][0]=='.')
    for j in range(n):
        max_dists_vert[0][j] = 1*(grid[0][j]=='.')
        
    for i in range(m):
        for j in range(n):
            not_marsh = grid[i][j]=='.'
            if i > 0:
                max_dists_vert[i][j] = max_dists_vert[i-1][j] + 1 if not_marsh else 0
            if j > 0:
                max_dists_horiz[i][j] = max_dists_horiz[i][j-1] + 1 if not_marsh else 0
    best_pair, best_pair_score = None, 0
    for i in range(m-1,0,-1):
        for j in range(n-1,0,-1):
            max_i = max_dists_vert[i][j]
            max_j = max_dists_horiz[i][j]
            
            if 2*(max_i+max_j-2) <= best_pair_score: continue
            
            for delta_i in range(max_i,1,-1):
                for delta_j in range(max_j,1,-1):
                    if 2*(delta_i+delta_j-2) <= best_pair_score: continue
                        
                    i2, j2 = i-delta_i+1, j-delta_j+1
                    p2_vert, p2_horiz = max_dists_vert[i][j2], max_dists_horiz[i2][j]
                    
                    if max_dists_vert[i][j2] >= delta_i and max_dists_horiz[i2][j] >= delta_j:
                        pair = [(i,j), (i2, j2)]
                        pair_score = 2*(delta_i + delta_j - 2)
                        if pair_score > best_pair_score:
                            best_pair, best_pair_score = pair, pair_score
                        
    if best_pair_score == 0:
        print("impossible")
    else:
        #print(best_pair)
        print(best_pair_score)

if __name__ == "__main__":
    first_input = input().rstrip().split()
    m = int(first_input[0])
    n = int(first_input[1])
    grid = []
    for _ in range(m):
        grid_item = input()
        grid.append(grid_item)
    kMarsh(grid)