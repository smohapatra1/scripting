#   https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/

def swap(List, pos1, pos2):
    List[pos1], List[pos2] = List[pos2], List[pos1]
    return List


if __name__ == "__main__":
    List = [23, 65, 19, 90]
    pos1 = 1
    pos2 = 2
    result = swap(List, pos1, pos2)
    print (result)