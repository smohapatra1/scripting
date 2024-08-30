#   https://www.geeksforgeeks.org/python-program-to-capitalize-the-first-and-last-character-of-each-word-in-a-string/

# Use title 
# Use splits 
# Indexed them with first and last item

def Caps(s):
    res = ''
    for i in s.title().split():
        res += (i[:-1] + i[-1].upper()) + ' '
    return res

if __name__ == "__main__":
    s = 'hello world'
    result = Caps(s)
    print (result)