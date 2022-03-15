#Draw a square of stars on a Screen
def while_loop():
    i=0
    while i < 3:
        stars = ""
        j = 0 
        while j < 3:
            stars += "* "
            j += 1 
        print (stars)
        i +=1 
def for_loop():
    for i in range(4):
        stars=""
        for j in range(4):
            stars +="* "
        print (stars)
#while_loop()
for_loop()
