#produt of arrary except self
#input [ 1,2,3,4]
#Output [24,12,8,6]

def array_except_self(x):
    length = len (x)
    l = [0] * length
    r = [0] * length
    p = [0] * length
    #print (length)
    l[0] = 1
    for i in range (1, length):
        l[i] = l[i-1] * x[i-1]
    print (l)
    r[length -1] = 1
    for j in range (length -2,-1,-1):
        r[j] = r[j+1] * x[j+1]
    print (r)
    for i in range(length):
        p[i] = l[i] * r[j]
    print(p)

array_except_self([10,3,5,6,2])


