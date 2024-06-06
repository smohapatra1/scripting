# Convert a list into a string 


def ListToString(n):
    string = ''.join(n)
    print (string)

if __name__ == "__main__":
    # n = input().split().rstrip()
    n = [ 'P', 'Y', 'T', 'H', 'O', 'N']
    res = ListToString(n)