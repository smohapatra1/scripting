#Write a Python function that takes a list and returns a new list with unique elements of the first list.

#Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]
def uniq(x):
    print (list(set(x)))
    seen_number = []
    for i in x:
        if i not in seen_number:
            seen_number.append(i)
    print (seen_number)
uniq([1,1,1,1,2,2,3,3,3,3,4,5])