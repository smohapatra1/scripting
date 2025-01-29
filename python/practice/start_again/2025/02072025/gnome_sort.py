#   https://www.geeksforgeeks.org/python-program-for-gnome-sort/

def GnomeSort(arr, n ):
    index = 0 
    while index < n :
        if index == 0:
            index = index +1 
        if arr[index] >=arr[index -1]:
            index = index +1 
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index = index - 1
    return
if __name__ == "__main__":
    arr = [34, 2, 10, -9]
    n = len(arr)
    print ("Original : ", arr)
    GnomeSort(arr, n )
    print ("new One  :", arr)