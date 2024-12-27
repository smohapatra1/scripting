#/usr/bin/python
#The task is to print a pattern as shown in the example for a given integer value.
'''
Input: N = 4
Output:
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
'''
a = int(input("Enter an Integer : "))
for i in range(1, a+1) :
    for j in range(1, a+1):
        x = i if i <    j else j
        y = a-x +1
        #print(a - x + 1, end = "");
        print ("%d %d %d %d %d " % ( a, y, i, j, a))
    print()
