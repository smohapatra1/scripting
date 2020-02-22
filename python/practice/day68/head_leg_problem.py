#Find chicken and dog - head and leg problem 
def animals(heads, legs):
    count = 0 
    count = (legs) - 2 * (heads)
    count = count/2
    return count

if __name__ == '__main__':
    heads=100
    legs=300
    animal = animals(heads, legs)
    #animal=animals(int(input("Num of heads : ")),int(input("Num of legs : ")))
    print ("Rabbits = ", animal)
    print ("Peigon = ", (heads - animal )) 
