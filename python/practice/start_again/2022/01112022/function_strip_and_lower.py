#Define a fucntion strip and lower
#This function should remove space at the begining and at the end of the string
# this it will convert the string into lower case
import string
import os
def strip_lower(a):
    remove_space=a.strip()
    print (f'{remove_space}')
    lower_text=remove_space.lower()
    #return lower_text
    print (f'{lower_text}')
strip_lower(" Samar Mohapatra ")
