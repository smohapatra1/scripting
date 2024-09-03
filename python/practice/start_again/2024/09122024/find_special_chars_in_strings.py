#   https://www.geeksforgeeks.org/python-program-check-string-contains-special-character/

#   Use Regex
#   Use Regex and compile 

import re
def Special(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if (regex.search(string) == None):
        print("String is accepted")
    else:
        print("String is NOT accepted")

if __name__ == "__main__":
    string = "Geeks$For$Geeks"
    result = Special(string)
    # print (result)