#   You are given a set of random numbers. Write a code to shift all the zeros to the left. 


def MoveZeros(a):
    read_index = len(a) -1 
    write_index = len(a) - 1 

    while read_index >= 0 :
        if a[read_index] != 0:
            a[write_index] = a[read_index]
            write_index -= 1 
        read_index -= 1
    while write_index >= 0 :
        a[write_index] = 0 
        write_index -=1
    return a

if __name__ == "__main__":
    a = [0, 1, 0, 3, 12, 0, 5]
    MoveZeros(a)
    print (a)


    
