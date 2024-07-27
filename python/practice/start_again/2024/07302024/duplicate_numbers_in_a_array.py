#   How Do You Find Duplicate Numbers in an Array With Multiple Duplicates?


def Duplicates(a):
    uniquelist = []
    duplist = []
    for i in a :
        if i not in uniquelist:
            uniquelist.append(i)
        elif i not in duplist:
            duplist.append(i)
    print (duplist)


if __name__ == "__main__":
    a = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
    result = Duplicates(a)