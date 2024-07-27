#   How Do You Find All Pairs in an Array of Integers That Add Up to a Specific Sum?

def specific_sum(a, sum ):
    for i in range(0, len(a) -1):
        for j in range(i+1, len(a)):
            if a[i] + a[j] == sum :
                print (a[i], "and" , a[j], "is equals to ", sum)
                break


if __name__ == "__main__":
    a = [ 5, 2, 1, 5, 8, 5, 1, 7, 7, 0 ]
    # a = [3, 4, 1, 2, 9]
    sum = 12 
    result = specific_sum(a, sum )
