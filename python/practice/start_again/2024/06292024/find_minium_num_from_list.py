# Finding minimum number from list 


def FindMinimum(n):
    MinNum = n[0]
    for i in n:
        if MinNum > i:
            MinNum = i 
    print (MinNum)

if __name__ == "__main__":
    n = input().rstrip().split()
    res = FindMinimum(n)
