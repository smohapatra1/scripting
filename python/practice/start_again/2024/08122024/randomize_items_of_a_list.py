#   Randomizing the Items of a List in Python

from random import shuffle

def Random(lst):
    shuffle(lst)
    print (lst)

if __name__ == "__main__":
    lst = ['Python', 'is', 'Easy']
    result = Random(lst)