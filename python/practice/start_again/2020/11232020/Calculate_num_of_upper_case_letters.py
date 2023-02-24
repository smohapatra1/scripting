#Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

#Sample String : 'Hello Mr. Rogers, how are you this fine Tuesday?'
#Expected Output : 
#No. of Upper case characters : 4
#No. of Lower case Characters : 33
def find_upper(x):
    x = x.replace(" ","")
    print (x)
    uppercase=0
    lowercase=0
    for char in x:
        if char.isupper():
            
            uppercase += 1
            
        elif char.islower():
            
            lowercase +=1
        else:
            pass
    print ("No of uppercase {}".format(uppercase))
    print ("Number of lowercase {}".format(lowercase))
find_upper("I am Good And Fine")