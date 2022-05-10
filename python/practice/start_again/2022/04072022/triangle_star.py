# Create different types of triagles 

# Right Triangle ( Lower Triangle ) - While loop
def right_triangle_while(n):
    i=0
    while i < n:
        star=""
        j=0
        while j <= i:
            star+=" *"
            j +=1
        print (star)
        i+=1
right_triangle_while(int(input("Enter the number of stars - while : ")))

#right triangle with for 
def right_triange_for(n):
    for i in range(n):
        star=""
        for j in range(i+1):
            star+=" *"
            j+=1
        print (star)
        i+=1

right_triange_for(int(input("Enter the number of stars - for : ")))

# Upper triangle with while 

def upper_triangle_while(n):
    i=0
    while i < n:
        star=" *"
        j=0
        while j <= i:
            star=" "
            j+=1
        print (star)
        i+=1
upper_triangle_while(int(input("Enter the number of stats - while : ")))