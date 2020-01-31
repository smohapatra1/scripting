#Number Pattern Example 4:
'''
 1
   2    1
   4    2    1
   8    4    2    1
  16    8    4    2    1
  32   16    8    4    2    1
  64   32   16    8    4    2    1
 128   64   32   16    8    4    2    1
 '''
def triag(x):
    for i in range (1,x):
        for j in range(-1+i,-1,-1):
            print (format(2**j, "4d"), end=" ")
        print ("\r")
triag(int(input("Enter the number : ")))
