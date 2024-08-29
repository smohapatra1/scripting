#   https://www.geeksforgeeks.org/find-length-of-a-string-in-python-4-ways/

def Slen(s):
    print (len(s))
    res = sum(1 for i in s)
    print (res)

if __name__ == "__main__":
    s = 'Samar is a good boy'
    result = Slen(s)
