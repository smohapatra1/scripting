#   https://www.geeksforgeeks.org/python-dictionary-exercise/?ref=outind
#   https://www.geeksforgeeks.org/python-dictionary-with-keys-having-multiple-inputs/
import random as rn

def Dict(x, y, z):
    dict = {}
    dict[x,y,z] = x + y - z
    x, y, z = 5, 2, 4
    dict[x,y,z] = x + y - z 
    return dict


if __name__ == "__main__":
    x, y, z = 10, 20, 30
    result = Dict(x, y, z)
    print (result)