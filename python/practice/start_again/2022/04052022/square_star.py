#Draw a square star using for loop
def square_star(n):
    for i in range(n):
        star =" "
        for j in range(n):
            star+=" *"
            j+=1
        print (star)
        i+=1
square_star(int(input("Enter the number of stars : ")))

def square_while(n):
    i=0
    while i < n:
        star=" "
        j=0
        while j <n:
            star+=" *"
            j+=1
        print (star)
        i+=1
square_while(int(input("Enter the number of stars : ")))
