# You are given a m x n 2D grid initialized with these three possible values.

# -1 - A wall or an obstacle. 0 - A gate. INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647. Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# For example, given the 2D grid:

# INF  -1  0  INF
# INF INF INF  -1
# INF  -1 INF  -1
#   0  -1 INF INF
# After running your function, the 2D grid should be:

#   3  -1   0   1
#   2   2   1  -1
#   1  -1   2  -1
#   0  -1   3   4

from typing import List
def wall_gates(rooms: List[List[int]]) -> None:
    if not rooms:
        return []
    row = len(rooms)
    col = len(rooms[0])
    directions=[(-1,0),(0,1),(1,0),(0,-1)]
    def dfs(x, y, dis):
        for dx, dy in directions:
            new_x=x+dx
            new_y=y+dy
            if 0<=new_x<row and 0 <=new_y<col and rooms[new_x][new_y]> rooms[x][y]:
                rooms[new_x][new_y] = dis+1
                dfs(new_x, new_y, dis+1)
    for x in range(row):
        for y in range(col):
            if rooms[x][y] == 0:
                dfs(x,y,0)
 
if __name__ == "__main__":
    rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    #Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
    print ("{}".format(wall_gates(rooms)))


 
