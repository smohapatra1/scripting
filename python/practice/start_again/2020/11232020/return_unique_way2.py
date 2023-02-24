#Write a Python function that takes a list and returns a new list with unique elements of the first list.
#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
def uniq(x):
    uNumber = []
    for nums in x:
        #print (nums)
        if nums not in uNumber:
           uNumber.append(nums)
    print (uNumber)
uniq([1,1,1,1,2,2,3,3,3,3,4,5])