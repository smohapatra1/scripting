#Print triange using list 
def triange(n):
    mynum= []
    for i in range(1,n):
        mynum.append("*"*i)
    print ("\n".join(mynum))

triange(int(input("Enter a number : ")))
