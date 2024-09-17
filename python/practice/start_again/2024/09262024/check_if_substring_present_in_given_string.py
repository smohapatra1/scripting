#   https://www.geeksforgeeks.org/check-if-string-contains-substring-in-python/

def Found(MyString1, Substring):
    if Substring in MyString1:
        print ("{} Found in {}".format(Substring, MyString1))
    else:
        print ("{} NOT Found in {}".format(Substring, MyString1))

if __name__ == "__main__":
    MyString1 = "A geek in need is a geek indeed"
    Substring = 'need1'
    result = Found(MyString1, Substring)
    