#   https://www.geeksforgeeks.org/python-check-if-string-contain-only-defined-characters-using-regex/

def FindChars(s, new_str):
    if re.search(pattern, s):
        print ("String matches")
    else:
        print ("String doesn't match")

if __name__ == "__main__":
    s = "876"
    # s = "987"
    pattern = re.compile('^[678]+$')
    FindChars(s, new_str)