#Write a function that takes one argument and return True if the passed value is even , False if it is not
def even(a):
    if a % 2 == 0:
        print ("{} is even ".format(a))
    else:
        print ("{} is odd".format(a))
even(10)