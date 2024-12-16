#   https://www.geeksforgeeks.org/python-program-to-count-uppercase-lowercase-special-character-and-numeric-values-using-regex/
import re

def Filter(s):
    uppercase = re.findall(r'[A-Z]', s)
    print ("Upper case counts are : ", len(uppercase))
    lowercase = re.findall(r'[a-z]', s)
    print ("Upper case counts are : ", len(lowercase))
    specialchar = re.findall(r'[@#$%&^*!,?. ]', s)
    print ("Specialchars counts are : ", len(specialchar))
    numchar = re.findall(r'[0-9]', s)
    print ("Numerical counts are : ", len(numchar))

if __name__ == "__main__":
    s = "ThisIsGeeksforGeeks!, 123"
    Filter(s)