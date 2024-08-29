#   https://www.geeksforgeeks.org/python-program-to-print-even-length-words-in-a-string/

def PrintEven(s):
    w = s.split(' ')
    # Solution - 01 
    # for i in w:
    #     if len(i) %2 == 0:
    #         print (i)
    # Solution - 02 
    print ([x for x in w if len(x) %2 == 0])

if __name__ == "__main__":
    s = "This is a python language"
    result = PrintEven(s)