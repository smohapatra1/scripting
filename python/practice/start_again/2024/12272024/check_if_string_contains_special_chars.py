#   https://www.geeksforgeeks.org/python-program-check-string-contains-special-character/

def CheckString(s):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(s) == None :
        print ("Valid")
    else:
        print ("Invalid")

if __name__ == "__main__":
    s = "Geeks"
    s1 = "G#@ks"
    CheckString(s)
    CheckString(s1)