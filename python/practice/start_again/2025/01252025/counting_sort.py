#   https://www.geeksforgeeks.org/problems/counting-sort/1
#   Given a string arr consisting of lowercase english letters, arrange all its letters in lexicographical order using Counting Sort.

from functools import reduce

def counting_sort(arr):
    sorted_str = reduce(lambda x, y: x+y, sorted(arr))
    return sorted_str
 
if __name__ == "__main__":
    arr = "geeksforgeeks"
    print("Sorted character array is ", arr )
