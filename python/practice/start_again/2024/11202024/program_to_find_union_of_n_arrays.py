#   https://www.geeksforgeeks.org/set-update-python-union-n-arrays/


def combineAll(input):
    s = set(input[0])
    for val in input[1:]:
        s.update(val)
    return list(s)

if __name__ == "__main__":
    input = [[1, 2, 2, 4, 3, 6],
            [5, 1, 3, 4],
            [9, 5, 7, 1],
            [2, 4, 1, 3]]
    print (combineAll(input))