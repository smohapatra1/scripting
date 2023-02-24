#take aribtary number and retun those arguments that are even 
def even(*args):
    x = []
    for i in args:
        if i%2 == 0:
            x.append(i)
    return x
    print (x)
even(1,2,3,4,5,6,7)
