#   https://www.geeksforgeeks.org/python-program-for-pigeonhole-sort/

def pigeonhole_sort(a): 
    my_min = min(a) 
    my_max = max(a) 
    size = my_max - my_min + 1
    holes = [0] * size 

    for x in a: 
        assert type(x) is int, "integers only please"
        holes[x - my_min] += 1
    i = 0
    for count in range(size): 
        while holes[count] > 0: 
            holes[count] -= 1
            a[i] = count + my_min 
            i += 1

a = [8, 3, 2, 7, 4, 6, 8] 
print("Orig Sorted order is : ", a) 
  
pigeonhole_sort(a) 
print("New Sorted order is : ", a) 
