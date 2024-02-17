# Find the median value form the list numbers 


def Median(arr):
    arr=sorted(arr)
    return arr[len(arr)//2]

if __name__ == "__main__":
    n=int(input().strip())
    arr=list(map(int, input().strip().split(' ')))
    res=Median(arr)
    print (res)