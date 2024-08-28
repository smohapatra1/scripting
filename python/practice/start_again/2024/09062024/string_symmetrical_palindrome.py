#   https://www.geeksforgeeks.org/python-program-to-check-whether-the-string-is-symmetrical-or-palindrome/?ref=leftbar-rightbar

def Symm(string):
    return string == string[::-1]
        
def Palin(string):
    mid = len(string)//2
    return string[:mid] == string[-mid:] 
if __name__ == "__main__":
    string = "amaama"
    # string = "khokho"
    if Symm(string):
        print ("{} is Palindrome".format(string))
    else:
        print ("{} is NOT Palindrome".format(string))
    if Palin(string):
        print ("{} is Symmetrical".format(string))
    else:
        print ("{} is NOT Symmetrical".format(string))