#   https://www.geeksforgeeks.org/python-check-if-a-given-string-is-binary-string-or-not/

def CheckString(s):
    p = set(s)
    s = {'0', '1'}
    if s == p or p == {'0'} == {'1'}:
        return 'Yes'
    else:
        return 'No'

if __name__ == "__main__":
    s = input("Enter a value : ")
    print ("The value %s is a string ? ", (s, CheckString(s)))