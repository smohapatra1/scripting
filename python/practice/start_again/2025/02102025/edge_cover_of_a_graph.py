#   https://www.geeksforgeeks.org/program-to-calculate-the-edge-cover-of-a-graph/

import math 
def EdgeCover(N):
    result = 0 
    result = math.ceil(N/2.0)
    return result

if __name__ == "__main__":
    N = 5 
    print (int(EdgeCover(N)))