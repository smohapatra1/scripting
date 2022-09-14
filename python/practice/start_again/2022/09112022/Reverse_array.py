#Reverse array

def reversearray(array):
    n=len(array)
    lowindex=0
    highindex=n-1
    while highindex > lowindex:
        array[lowindex], array[highindex] = array[highindex], array[lowindex]
        lowindex+=1
        highindex-=1


if __name__ == '__main__':
    array=[1,2,3,4,5]
    reversearray(array)
    print (array)