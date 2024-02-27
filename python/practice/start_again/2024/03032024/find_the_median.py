#   https://www.hackerrank.com/test/flgjjnhfm7i/questions/a8taf02a12a


def Median(arr):
    arr=sorted(arr)
    return arr[len(arr)//2]

if __name__ == "__main__":
    n=int(input().split())
    arr=list(map(int, input().strip().split(' ')))
    result=Median(arr)
    print (result)