#The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .
# Example 

# The list of non-negative integers that are less than  is . Print the square of each number on a separate line.
# 0
# 1
# 4

if __name__ =='__main__':
    i=0
    a=int(input())
    if a <= 0 :
        print ("Please enter a positive number : ")
    else:
        i=0
        for i in range(0,a):
            print (f"Value is {i} and its square is : {i**2}") 

