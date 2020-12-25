def myfunc(*args):
    print (args)
    x = []
    for i in args:
        if i%2 == 0:
            x.append(i)
    print (x)
    return x

#def myfunc(*args):
#    print ([n for n in args if n%2 == 0])
myfunc(1,2,3,45,6)
