#Write a Python function to multiply all the numbers in a list.

#Sample List : [1, 2, 3, -4]
#Expected Output : -24

def multiplyList(x):
    total = 1
    for i in x:
        total = i * total
    print (total)
multiplyList([1, 2, 3, -4])