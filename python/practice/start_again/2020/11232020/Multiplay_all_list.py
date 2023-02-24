#Write a Python function to multiply all the numbers in a list.
#Sample List : [1, 2, 3, -4]
#Expected Output : -24
def multiply(x):
    total = 1
    for i in x:
        total = i*total
    print ("Total {}".format(total))
multiply([1, 2, 3, -4])