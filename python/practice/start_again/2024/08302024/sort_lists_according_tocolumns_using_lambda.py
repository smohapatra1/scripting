#   https://www.geeksforgeeks.org/python-program-to-sort-the-list-according-to-the-column-using-lambda/

def sortedArray(array):
    for i in range(len(array[0])):
        sortedColumn = sorted(array, key = lambda x:x[i])
        print ("Sorted array specific to column {}, \ {}".format(i, sortedColumn))


if __name__ == "__main__":
    # array = [['java', 1995], ['c++', 1983],
            #  ['python', 1989]]
    array = [[1, 3, 3], [2, 1, 2], [3, 2, 1]] 
    sortedArray(array)