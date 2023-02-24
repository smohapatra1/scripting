#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output : 
#No. of Upper case characters : 4
#No. of Lower case Characters : 33

def count_letter(x):
    lowercase = 0 
    uppercase = 0 
    for letters in x:
        if letters.isupper():
            print (letters)
            uppercase += 1
        elif letters.islower():
            lowercase +=1
        else:
            pass
    print (x)
    print ("Num of big letters are {} and '{}'".format(uppercase,x))
    print ("Num of small letters are {} and '{}'".format(lowercase,x))
    
count_letter("I am GoooD")

#Incomplete 
