
#Problem 1
#Handle the exception thrown by the code below by using try and except blocks.

#In [1]:
#for i in ['a','b','c']:
#    print(i**2)
def problem1():
    try:
        for i in ['a','b','c']:
        #for i in [1,2,3]:
            print (i**2)
    except:
        print ("TypeError occoured")
    finally:
        print ("I am done")
if __name__ == "__main__":
    problem1()