num1 = []
def my_list(num1):
    print (num1)
    count = 0 
    for i in num1:
        print (i)
        count = count + i
        i +=1
    print ("And the sum is %d " % count)
my_list(input("Enter the numbers for the list "))

