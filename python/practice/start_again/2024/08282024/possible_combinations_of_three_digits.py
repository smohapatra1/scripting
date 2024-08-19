#   https://www.geeksforgeeks.org/python-program-to-print-all-possible-combinations-from-the-three-digits/

from itertools import permutations
def Combinations(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if (i != j and i != k and j != k ):
                    print (lst[i], lst[j], lst[k])

if __name__ == "__main__":
    lst = [1, 2, 3, 4]
    result = Combinations(lst)