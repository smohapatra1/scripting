#   Removing All Whitespace in a String
import re

def RemWhite(string):
    result = re.sub(re.compile(r'\s+'),'', string)
    print (result)


if __name__ == "__main__":
    string = "C O D E      Q"
    result = RemWhite(string)