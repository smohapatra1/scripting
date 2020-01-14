#Write a program to find maximum of a list.
def max_num(a):
#Using max function
    b = max(a)
    print ("Max number using Max  %d " %b)

#Using sort
    b = a.sort()
    print ("Max number using Sort % d" % a[-1])

#Using Not Max function
    my_max = a[0]
    for i in a:
        if i > a[0]:
            my_max = i 
    print ("Max Number using Not functions %d" % my_max)

max_num([1,2,3,4,10,123455,1261718181,1,1,1,1,1,7161617167178])

