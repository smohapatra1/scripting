#Write a function which accepts an input list of numbers and returns a list 
#which includes only the even numbers in the input list. 
#If there are no even numbers in the input numbers then your function should return an empty list.
def even_list(n):
    even_number =[]
    odd_number = []
    for i in n:
        if i % 2 == 0 :
            even_number.append(i)
        else:
            odd_number.append(i)
    print ("Even num lists %s" % even_number)
    print ("Odd num lists %s" % odd_number)
even_list(input("Enter numbers in list format "))

