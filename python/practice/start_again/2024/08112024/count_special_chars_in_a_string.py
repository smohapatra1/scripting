#   Counting Special Characters in a String
import re
def SpecialChars(n):
    count = re.sub('[\w]+', '', n)
    return len(count)

if __name__ == "__main__":
    n = "!@#$%^&*()$$$$"
    result = SpecialChars(n)
    print (result)