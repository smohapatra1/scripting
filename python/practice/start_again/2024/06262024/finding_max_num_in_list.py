# Finding the max Number in a list 

def MaxNum(n):
    maxNum = n[0]
    for i in n:
        if maxNum < i:
            maxNum = i 
    print (maxNum)


if __name__ == "__main__":
    n=input().rstrip().split()
    result=MaxNum(n)