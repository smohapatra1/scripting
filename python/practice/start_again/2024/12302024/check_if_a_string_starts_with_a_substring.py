#   https://www.geeksforgeeks.org/how-to-check-if-a-string-starts-with-a-substring-using-regex-in-python/
import re

def MatchSubstring(String, Substring):

    if Substring in String:
        y = "^" + Substring
        x = re.search(y, String)
        if x : 
            print ("String starts with the given substring")
        else:
            print ("String doesn't starts with given substring")
    else:
        print ("Entered string isn't a substring")
if __name__ == "__main__":
    String = "geeks for geeks makes learning fun" 
    # Substring = "geeks" 
    Substring = "makes"
    MatchSubstring(String, Substring)