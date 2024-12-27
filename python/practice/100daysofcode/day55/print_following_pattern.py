''' 
print following pattern
0 
2 4 
4 8 8 
8 16 16 16
'''
def pat(x):
    counter=0
    for i in range(0,x):
        for j in range(0, i+1):
            print(counter, end=" ")
            counter=2**(i+1)
        print("\r")

pat(int(input("Enter a number : ")))
