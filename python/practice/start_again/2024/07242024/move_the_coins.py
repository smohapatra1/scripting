# #   https://www.hackerrank.com/challenges/move-the-coins/problem?isFullScreen=true

# Alice and Bob are playing a game, defined below:

# There is an undirected tree graph with  nodes that has the following properties:
# Each node has  golden coins.
# Node  is root of the tree.
# The parent node of some node  is defined as .
# Moves
# Players move in turns.
# During a move, a player can select a node  and move one or more coins to .
# If the current player can't make any move, they lose the game.
# The game quickly becomes boring because the result is determined by the tree's configuration and the number of coins in each node (assuming that both players play optimally).

# Alice decides to instead challenge Bob by asking him  questions. For each question :

# Alice picks a node  and removes the edge between  and .
# She picks another node  and draws a new undirected edge between  and . So now .
# Bob must determine if the first player has a winning strategy for the new tree or not. It's possible that after Alice draws the new edge, the graph will no longer be a tree; if that happens, the question is invalid. Each question is independent, so the answer depends on the initial state of the graph (and not on previous questions).

# Given the tree and the number of coins in each node, can you help Bob answer all  questions?

# Input Format

# The first line contains an integer,  (the number of nodes).
# The second line contains  space-separated integers, , describing the number of coins in each node.
# Each of the  subsequent lines contains  space-separated integers denoting an undirected edge between nodes  and , respectively.
# The next line contains an integer,  (the number of questions Alice asks).
# Each of the  subsequent lines contains  space-separated integers,  and , respectively.

# Constraints

# For each question:

# Output Format

# On a new line for each question, print  if the first player has a winning strategy, print  if they do not, or print  if the question is not valid.

# Sample Input

# 6
# 0 2 2 1 3 2
# 1 2
# 1 3
# 3 4
# 3 5
# 4 6
# 3
# 6 2
# 4 1
# 3 6
# Sample Output

# NO
# YES
# INVALID
# Explanation

# Initally the tree looks like this: goldenagain.png

# After the first question (), the tree looks like this: goldenagain(1).png Alice removes the edge conecting node  to  and makes  the new parent node of . Because this configuration does not result in a winning strategy, we print  on a new line.

# After the second question (), the tree looks like this: goldenagain(5).png Alice removes the edge conecting node  to  and makes  the new parent node of . Because this configuration results in a winning strategy, we print  on a new line.

# After the third question (), the graph is no longer a tree: goldenagain(6).png Alice removes the edge conecting node  to  and makes  the new parent node of . The graph is now partitioned into two separate subgraphs (one of which is also not a tree); because the game must be played on a single undirected tree graph, we print  on a new line.

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

n = int(input())
G = [[int(c), 0, []] for c in input().strip().split()]
G[0][2].append(0)
parity = [True for i in range(n)]
order = [[-1,-1] for i in range(n)]
for i in range(n-1):
    v1, v2 = (int(v)-1 for v in input().strip().split())
    G[v1][2].append(v2)
    G[v2][2].append(v1)
total = 0
pre = 0
post = 0
parent = deque([0])
while (len(parent) > 0):
    node = parent.pop()
    if (order[node][0] == -1):
        order[node][0] = pre
        pre += 1
        parity[node] = not parity[G[node][1]]
        if (parity[node]):
            total = total ^ G[node][0]
        G[node][2].remove(G[node][1])
        if (len(G[node][2]) == 0):
            parent.append(node)
        else:
            for c in G[node][2]:
                G[c][1] = node
                parent.append(c)
    else:
        order[node][1] = post
        post += 1
        for c in G[node][2]:
            G[node][0] = G[node][0] ^ G[c][0]
        if (G[G[node][1]][2][0] == node):
            parent.append(G[node][1])
                
q = int(input())
for i in range(q):
    u, v = (int(vertex)-1 for vertex in input().strip().split())
    if (order[u][0] < order[v][0] and order[u][1] > order[v][1]):
        print("INVALID")
    elif (parity[u] == parity[v]):
        newtotal = G[u][0]
        if (newtotal ^ total == 0):
            print("NO")
        else:
            print("YES")
    else:
        if (total == 0):
            print("NO")
        else:
            print("YES")
