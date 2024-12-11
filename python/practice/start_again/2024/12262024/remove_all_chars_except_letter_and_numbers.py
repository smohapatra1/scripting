#   https://www.geeksforgeeks.org/python-remove-all-characters-except-letters-and-numbers/

import re

def RemoveAllChar(ini_string):
    print (re.sub('[\W_]+', '', ini_string))

if __name__ == "__main__":
    ini_string = "abcjw:, .@! eiw123"
    RemoveAllChar(ini_string)