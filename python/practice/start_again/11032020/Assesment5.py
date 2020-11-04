
#Write a program that prints the integers from 1 to 100. 
#But for multiples of three print "Fizz" instead of the number, 
#and for the multiples of five print "Buzz". 
#For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1,101):
    if (i % 3 == 0) and (i % 5 == 0) :
        print ("Number is {} and word {} ".format (i, 'FizzBuzz'))
    elif i % 3 == 0:
        print ("Number is {} and word {} ".format (i, 'Fizz'))
    elif i % 5 == 0:
        print ("Number is {} and word {} ".format (i, 'Buzz'))
    else:
        print ("Number {}".format(i))
    