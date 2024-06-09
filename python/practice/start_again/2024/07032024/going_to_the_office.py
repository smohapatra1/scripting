# #   https://www.hackerrank.com/challenges/going-office/problem?isFullScreen=true

# Ms.Kox enjoys her job, but she does not like to waste extra time traveling to and from her office. After working for many years, she knows the shortest-distance route to her office on a regular day.

# Recently, the city began regular maintenance of various roads. Every day a road gets blocked and no one can use it that day, but all other roads can be used. You are Ms. Kox's new intern and she needs some help. Every day, you need to determine the minimum distance that she has to travel to reach her office.

# Input Format

# There are N cities numbered 0 to N-1 and M bidirectional roads.

# The first line of the input contains two integers N and M.
# M lines follow, each containing three space-separated integers u , v and w, where u and v are cities connected by a bi-directional road and w is the length of this road. There is at most one road between any two cities and no road connects a city to itself.
# The next line contains two integers S and D. S is the city where Ms. Kox lives and D is the city where her office is located.
# The next line contains an integer Q, the number of queries.
# Q lines follow, each containing two integers u and v, where the road between u and v has been blocked that day.
# Constraints






# Output Format

# Output Q lines, with each line containing the minimum distance Ms.Kox has to travel on that day. If there is no path, print "Infinity".

# Sample Input

# 6 9  
# 0 1 1  
# 1 2 1  
# 2 3 1  
# 3 4 1  
# 4 5 1  
# 2 4 5  
# 3 5 8  
# 1 3 3  
# 0 2 4  
# 0 5  
# 9  
# 0 1  
# 1 2  
# 2 3  
# 3 4  
# 4 5  
# 2 4  
# 3 5  
# 1 3  
# 0 2
# Sample Output

# 7  
# 6  
# 6  
# 8  
# 11  
# 5  
# 5  
# 5  
# 5


# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import copy
from heapq import heappush, heappop

cities, roads = map(int, input().split())
graph = {n: [] for n in range(cities)}
edges = []
for road in range(roads):
    fr, to, dist = map(int, input().strip().split())
    edges.append((fr, to, dist))
    graph[fr].append((to, dist))
    graph[to].append((fr, dist))
graph_copy = copy.deepcopy(graph)
start, finish = map(int, input().strip().split())
number_of_queries = int(input().strip())
queries = []
for q in range(number_of_queries):
    queries.append(tuple(map(int, input().strip().split())))


def min_path_length(g, s, f):

    city_list = [{'visited': False, 'dist': math.inf} for c in range(cities)]

    pq = []
    heappush(pq, (0, s))
    city_list[s]['dist'] = 0

    while pq:
        current_dist, current_city = heappop(pq)
        if city_list[current_city]['visited']:
            continue
        city_list[current_city]['visited'] = True
        # if current_city == f:
        #     break
        for neighbor in g[current_city]:
            if not city_list[neighbor[0]]['visited']:
                old_dist = city_list[neighbor[0]]['dist']
                new_dist = current_dist + neighbor[1]
                if new_dist < old_dist:
                    heappush(pq, (new_dist, neighbor[0]))
                    # pq.sort()
                    city_list[neighbor[0]]['dist'] = new_dist

    return [x['dist'] for x in city_list]


def optimal_edges(edges, ds, dt, opt):
    result = {}
    for edge in edges:
        u, v, dist = edge
        if ds[u] + dist + dt[v] == opt:
            result[(u, v)] = dist
        if ds[v] + dist + dt[u] == opt:
            result[(v, u)] = dist
    return result

    
def bridges(opt_edges, ds, opt):
    result = {}
    sorted_nodes = sorted([((ds[u], ds[v]), (u, v)) for u, v in opt_edges.keys()])
    sorted_nodes = [((0, 0), (start, start)), *sorted_nodes, ((opt, opt), (finish, finish))]
    for i in range(1,len(sorted_nodes) - 1):
        if sorted_nodes[i][0][0] >= sorted_nodes[i-1][0][1] and sorted_nodes[i][0][1] <= sorted_nodes[i + 1][0][0]:
            result[sorted_nodes[i][1]] = opt_edges[sorted_nodes[i][1]]
    return result


def arrowed_graph(edges, ds):
    a_graph = {n: [] for n in range(cities)}
    for (u, v, dist) in edges:
        if ds[u] + dist == ds[v]:
            a_graph[u].append(v)
        if ds[v] + dist == ds[u]:
            a_graph[v].append(u)
    return a_graph


def islands(ag, bridges):
    isl = [0] * cities
    sorted_bridges = sorted([((ds[u], ds[v]), (u, v)) for u, v in bridges.keys()],)
    sorted_bridges_ends = [v for ((dsu, dsv),(u, v)) in sorted_bridges]

    def dfs(fr, ag, island_id):
        stack = []
        stack.append(fr)
        while stack:
            current_node = stack.pop()
            isl[current_node] = island_id
            for node in ag[current_node]:
                if isl[node] == 0:
                    stack.append(node)
        return isl

    isl_count = len(bridges) + 1

    for i in reversed(sorted_bridges_ends):
        dfs(i, ag, isl_count)
        isl_count -= 1

    dfs(start, ag, isl_count)

    return isl


def bypasses(edges, bridges, islands, ds, dt):
    result = {(u, v): math.inf for u, v in bridges.keys()}
    island_to_bridge = {min(islands[u], islands[v]): (u, v) for u, v in bridges}
    edges_to_iterate = {(u, v): dist for u, v, dist in edges if (u, v) not in bridges.keys() and (v, u) not in bridges.keys()}
    for (u, v) in edges_to_iterate.keys():
        if islands[u] < islands[v]:
            for i in range(islands[u], islands[v]):
                result[island_to_bridge[i]] = min(result[island_to_bridge[i]], ds[u] + edges_to_iterate[(u, v)] + dt[v])
        if islands[v] < islands[u]:
            for i in range(islands[v], islands[u]):
                result[island_to_bridge[i]] = min(result[island_to_bridge[i]], ds[v] + edges_to_iterate[(u, v)] + dt[u])

    return result


ds = min_path_length(graph, start, finish)
dt = min_path_length(graph, finish, start)

opt = ds[finish]

opt_edges = optimal_edges(edges, ds, dt, opt)
br = bridges(opt_edges, ds, opt)
ag = arrowed_graph(edges, ds)
isl = islands(ag, br)
bp = bypasses(edges, br, isl, ds, dt)

for u, v in queries:
    if (u, v) in br:
        print(bp[(u, v)] if bp[(u, v)] < math.inf else 'Infinity')
    elif (v, u) in br:
        print(bp[(v, u)] if bp[(v, u)] < math.inf else 'Infinity')
    else:
        print(opt)