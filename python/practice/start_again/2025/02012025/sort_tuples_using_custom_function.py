

def Sort(a):
    return sorted(a)


if __name__ == "__main__":
    a = ([2, 1, 5], [1, 5, 7], [5, 6, 5])
    print ("Unsorted : ", a )
    sorted_tuple=tuple(map(Sort, a))
    print ("Sorted   : ", sorted_tuple )