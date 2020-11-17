#OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name
#old_macdonald('macdonald') --> MacDonald
def caps(a):
    first_letter=a[0]
    inbetwen_letter=a[1:3]
    fouth_letter=a[3]
    rest_letter=a[4:]
    print ("Metho1 : {}".format(first_letter.upper() + inbetwen_letter + fouth_letter.upper() + rest_letter))

#Method02 - Using capitalize 
    first_half=a[:3]
    second_half=a[3:]
    print ("Method2 : {}".format(first_half.capitalize() + second_half.capitalize()))
caps('samarendra')