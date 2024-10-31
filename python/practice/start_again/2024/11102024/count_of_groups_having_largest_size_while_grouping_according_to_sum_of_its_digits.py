# https://www.geeksforgeeks.org/count-of-groups-having-largest-size-while-grouping-according-to-sum-of-its-digits/?ref=leftbar-rightbar

def constDict(n):
    d = {}
    for i in range(1, n+1):
        s = str(i)
        l = list(s)
        sum1 = sum(map(int, 1))
        if sum1 not in d:
            d[sum1] = 1
        else:
            d[sum1] += 1
    return d

def countLargest(n):
    d = constDict(n)
    size = 0 
    count = 0 
    for k, val in d.items():
        if val > size: 
            size = val 
            count = 1
        elif val == size:
            count +=1
    return count 

if __name__ == "__main__":
    n = 13
    group = countLargest(n)
    print(group)
