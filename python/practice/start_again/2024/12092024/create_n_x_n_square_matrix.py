#   https://www.geeksforgeeks.org/create-an-n-x-n-square-matrix-where-all-the-sub-matrix-have-the-sum-of-opposite-corner-elements-as-even/

import itertools
def sub_mat_even(n):
    temp = itertools.count(1)
    m = [ [ next(temp) for i in range(n)] for i in range(n)]
    if n % 2 == 0:
        for i in range(0, len(m)):
            if i % 2 == 1 :
                m[i][:] = m[i][::-1]
    for i in range(n):
        for j in range(n):
            print (m[i][j], end = " ")
        print ()


if __name__ == "__main__":
    n = 4
    sub_mat_even(n)
