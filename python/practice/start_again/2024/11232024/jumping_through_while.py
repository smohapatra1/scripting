#   https://www.geeksforgeeks.org/problems/jumping-through-while-python/1

def Jump(x):
    n = 1 
    while ((n**2) <= x ):
        print ((n**2), end = " ")
        n +=1
if __name__ == "__main__":
    x = 100 
    Jump(x)