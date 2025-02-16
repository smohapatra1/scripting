#   https://www.geeksforgeeks.org/program-to-calculate-the-edge-cover-of-a-graph/

import math

def edgeCover(n):
    result = 0
    result = math.ceil(n/2.0)
    return result 

if __name__ == "__main__":
    n = 5 
    print (int(edgeCover(n)))