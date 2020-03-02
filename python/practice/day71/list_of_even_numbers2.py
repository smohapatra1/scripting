#List Methods Exercise 8 (List of Even Numbers)
#0 points possible (ungraded)
#Write a function that accepts two positive integers a and b and returns a list of all the even numbers between a and b (including a and not including b).
def even(x,y):
    list=[]
    for i in range (x,y):
        if i % 2 == 0:
            list.append(i)
    print (list)

even(int(input("Enter num -a : ")),int(input("Enter 2nd num - b : ")))
