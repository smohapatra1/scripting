# Find a perfect number
def perfect(x):
    sum = 1
    i = 2
    while i * i <= int(x):
        if int(x) % i == 0:
            sum = sum + i + int(x)/i
        i +=1
    if sum == int(x) :
        print (x, " is a perfect number")
    else:
        print (x, "is NOT a perfect number")

perfect(input("Enter a number : "))
