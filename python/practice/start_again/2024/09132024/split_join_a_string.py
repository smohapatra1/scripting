#   https://www.geeksforgeeks.org/python-program-split-join-string/

def SplitJoin(string):
    s = string.split(' ')
    print (s)
    t = '-'.join(s)
    print (t)

if __name__ == "__main__":
    string = 'Geeks for Geeks'
    result = SplitJoin(string)