x = [1,4,5,8,10,20]
from random import shuffle
shuffle(x)
print ("One way to shuffle {}".format(x))

def shuffle_list(mylist):
    shuffle(mylist)
    return mylist
result = shuffle_list(x)
print ("2nd way is {}".format(result))