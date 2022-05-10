#Print ISOSCELES stars

def isosceles_for(n):
    for i in range(n):
        stars=""
        for j in range(i+1):
            stars+="* "
        print (stars)
    for i in range(n,0,-1):
        stars=""
        for j in range(i):
            stars+="* "
        print (stars)
isosceles_for(int(input("Enter the number of stars: ")))