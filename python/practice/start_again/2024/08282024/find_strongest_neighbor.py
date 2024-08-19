#   https://www.geeksforgeeks.org/python-program-to-find-the-strongest-neighbour/

def Neighbor(test_list):
    size = len(test_list)
    res = []
    for i in range(1, size):
        r = max(test_list[i], test_list[i-1])
        res.append(r)
    for ele in res:
        print (ele, end=' ')


if __name__ == "__main__":
    test_list = [1, 2, 2, 3, 4, 5]
    result = Neighbor(test_list)