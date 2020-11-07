def val (**kwargs):
    print (kwargs)
    if 'fruit' in kwargs:
        print ("My Fav fruit is {}".format(kwargs['fruit']))
    else:
        print ("I dont have a choice")
val(fruit='apple', veg = 'potato')