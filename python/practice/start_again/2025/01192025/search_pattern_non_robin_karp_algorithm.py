#   https://www.geeksforgeeks.org/problems/search-pattern-rabin-karp-algorithm--141631/1?page=1&category=Pattern%20Searching&sortBy=submissions
import re

def Indices(text, pattern):
    matches = re.finditer(pattern, text)
    res = [match.start() for match in matches]
    return res

if __name__ == "__main__":
    text = "birthdayboy"
    pattern = "birth"
    text1 = "geeksforgeeks"
    pattern1 = "geek"
    print (Indices(text, pattern))
    print (Indices(text1, pattern1))
