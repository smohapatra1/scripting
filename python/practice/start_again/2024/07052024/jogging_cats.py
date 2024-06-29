# https://www.hackerrank.com/challenges/cat-jogging/problem?isFullScreen=true

# It's almost summertime, so Big Cat and Little Cat are getting in shape. They decide the core of their fitness plan is to start jogging every day.

# Their city consists of  intersections connected by  bidirectional roads. The cats decide that their jogging route should be cyclic (i.e., starting and ending at the same intersection) and consist of  different roads.

# The cats also love exploring new places, so each day they want to choose a new route to jog on that is not equal to any of their previous routes. Two routes are considered to be equal if their sets of component roads are equal.

# Given a map of the city, can you help our heroic cats determine the maximum number of days they can go jogging so that every route traveled is different?

# Input Format

# The first line contains a pair of space-separated integers,  (the number of intersections) and  (the number of roads), respectively.

# Each line  of the  subsequent lines contains a pair of space-separated integers,  and , defining a bidirectional road connecting intersections  and .

# Constraints

# Each bidirectional road connects  distinct intersections (i.e., no road connects an intersection to itself).
# Each pair of intersections is directly connected by no more than  road.
# Output Format

# Print the maximum number of days for which the cats can go jogging without repeating a route.

# Sample Input

# 4 6
# 1 2
# 2 3
# 3 4
# 4 1
# 1 3
# 2 4
# Sample Output

# 3
# Explanation

# There are  different routes:

# Recall that each route is a set of intersections forming a cycle, so each unique route is the same regardless of which city on the route the cats start out at. Thus, we print  (the number of routes) as our answer.




def joggingCats(n,m,graph):
    result = 0
    visited = set([])
    for source,destinations in graph.items():
        destinationCount = {}
        for x in destinations:
            if x not in visited and x in graph:
                for y in graph[x]:
                    if y not in visited:
                        try:
                            destinationCount[y] += 1
                        except:
                            destinationCount[y] = 1
        for node,count in destinationCount.items():
            if node != source:
                result+= count*(count-1)//2
        visited.add(source)
    return result


if __name__ == '__main__':

    n,m =  [int(i) for i in input().strip().split()]
    graph = {}
    for _ in range(m):
        x,y = [int(i) for i in input().strip().split()]
        try:
            graph[x].append(y)
        except:
            graph[x] = [y]
        try:
            graph[y].append(x)
        except:
            graph[y] = [x]
    print(joggingCats(n,m,graph))