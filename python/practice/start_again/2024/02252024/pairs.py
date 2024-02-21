#   https://www.hackerrank.com/test/ebch3feom7p/questions/g2lt30pl1g0


def pairs(k, arr):
    my_dict={}
    result = 0 
    for ele in arr:
        my_dict[ele] = 1
        if ele+k in my_dict:
            result +=1
        if ele-k in my_dict:
            result +=1
    return result


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    result = pairs(k, arr)
    print (result)