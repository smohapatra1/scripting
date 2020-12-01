#Write a Python function that checks whether a passed in string is palindrome or not.

#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def palindrome(x):
    #Remove the spaces 
    x = x.replace(' ', '')
    print (x)
    if x == x[::-1]:
        print ( "{} is palindrome".format(x) )
    else:
        print ("{} is NOT palindrome".format(x))
palindrome('xyx')