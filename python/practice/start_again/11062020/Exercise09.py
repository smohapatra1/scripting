#take aribtary number and retun those arguments that are even 
def even(*args):
    for i in args:
        if i % 2 == 0:
            print (i)
        #else:
        #    print ("Odd")
even(1,2,3,4,5,6,7)