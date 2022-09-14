#Reverse an Integer - > 1234 - > 4321




def reverse_int(a):
    reversed=0
    reminder=0
    while a > 0 :
        reminder=a%10
        a=a//10
        reversed=reversed * 10 +reminder
    #return reversed
    print (reversed)


if __name__ == '__main__':
    a=int(input("Enter an integer : "))
    reverse_int(a)
    #print (a)
    