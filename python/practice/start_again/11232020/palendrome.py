#Write a Python function that checks whether a passed in string is palindrome or not.
#Note: A palindrome is word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
def palendrone(x):
    x = x.replace(" ", "")
    if x == x[::-1]:
        print ( "This {} is palindrome".format(x))
    else:
        print ("This {} is NOT palindrome".format(x))
palendrone("nurses run")