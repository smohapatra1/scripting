#Prime number with range of values
for i in range(1,200):
    for v in range(2, i):
        if (i % v ) == 0 :
            break
    else:
        print (i)
