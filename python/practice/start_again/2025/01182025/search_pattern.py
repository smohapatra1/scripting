#   https://www.geeksforgeeks.org/problems/search-pattern0205/1?page=1&category=Pattern%20Searching&sortBy=submissions
#   Given two strings, one is a text string txt and the other is a pattern string pat. 
#   The task is to print the indexes of all the occurrences of the pattern string in the text string. Use 0-based indexing while returning the indices. 
#   Note: Return an empty list in case of no occurrences of pattern.

def printIndex(txt, pat):
    pos = txt.find(pat)
    if pos == -1:
        print("NONE")
    while pos != -1:
        print(pos, end=" ")
        pos = txt.find(pat, pos + 1)


if __name__ == "__main__":
    txt = "abcab"
    pat = "ab"
    txt1 = "abesdu"
    pat1 = "edu"
    printIndex(txt, pat)
    printIndex(txt1, pat1)