def myfunc(a):
    out = []
    for i in range(len(a)):
        if i%2 == 0:
            out.append(a[i].upper())
        else:
            out.append(a[i].lower())
    return ''.join(out)
myfunc('Samarendra')