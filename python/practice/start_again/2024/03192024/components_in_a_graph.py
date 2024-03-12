#   https://www.hackerrank.com/test/g9a39gf8b53/questions/b7ng6ogbtm

#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'componentsInGraph' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY gb as parameter.
#

def componentsInGraph(gb):
    # Write your code here
    clusters=[]
    for edge in gb:
        clusters_to_fuse=[]
        for cluster in clusters:
            if edge[0] in cluster or edge[1] in cluster:
                clusters_to_fuse.append(cluster)
        if clusters_to_fuse:
            fused_cluster=set(edge)
            for cluster in clusters_to_fuse:
                for node in cluster:
                    fused_cluster.add(node)
                clusters.remove(cluster)
            clusters.append(fused_cluster)
        else:
            clusters.append(set(edge))
    clusters_len=list(map(len, clusters))
    return [min(clusters_len), max(clusters_len)]
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
