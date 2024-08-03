#   Finding the Maximum Number in a List

def MaxNum(a):
    Max = a[0]
    for i in a:
        if Max < i :
            Max = i 
    return Max

if __name__ == "__main__":
    a = [1, 9, 10, 12, 15, 50]
    result = MaxNum(a)
    print (result)