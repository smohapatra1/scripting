#   https://www.geeksforgeeks.org/creating-multiple-constructors-python-class/

# Class - 1

class X:
    def __init__(self):
        print ('One')
    def __init__(self):
        print ('Two')
    def __init__(self):
        print ('Three')
e = X()

# Class - 2 

class Test:
    def __init__(self, *args):
        if len(args) > 1 :
            self.ans = 0 
            for i in args:
                self.ans += i 
        elif isinstance(args[0], int):
            self.ans = args[0]*args[0]
        elif isinstance(args[0], str):
            self.ans = "Hello! "+ args[0]+"."
s1 = Test(1, 2, 3, 4, 5)
print ("Sum list :", s1.ans)
s2 = Test(5)
print ("Square of int : ", s2.ans)
s3 = Test("Samar")
print ("String: ", s3.ans)


