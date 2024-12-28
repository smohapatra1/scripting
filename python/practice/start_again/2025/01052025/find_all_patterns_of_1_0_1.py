#   https://www.geeksforgeeks.org/find-patterns-101-given-string-using-python-regex/

def extract(s):
    count = 0 
    a = re.search('10+1', s )
    while a != None:
        count = count+1 
        s = s[(a.end()-1):]
        a = re.search('10+1', s)
    print (count)

if __name__ == "__main__":
    s = '1101001'
    s1 = '1abc101'
    extract(s)
    extract(s1)