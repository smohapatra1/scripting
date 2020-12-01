#Write a Python function to check whether a string is pangram or not.

#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
#For example : "The quick brown fox jumps over the lazy dog"
def pangram(x):
    letters = 0
    #Make set up alphabets 
    #x = list(set(x))
    #print (x)
    #Remove Space
    x = x.replace(' ', '')
    print (x)
    #Make them lower 
    x = x.lower()
    #print (x)
    x = list(set(x))
    x = list(x)
    print (x)
pangram("The quick brown fox jumps over the lazy dog")

# Not complete fully 