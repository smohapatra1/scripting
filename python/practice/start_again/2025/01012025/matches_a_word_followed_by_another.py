#   https://www.geeksforgeeks.org/python-program-that-matches-a-word-containing-g-followed-by-one-or-more-es-using-regex/

def MatchWord(s):
    regex = re.compile("ge\w*")
    match = regex.findall(s)
    if len(match) != 0 :
        for word in match:
            print (word)
    else:
        print ("No Match")

if __name__ == "__main__":
    s = 'geeks for geeks'
    s1 = "I am good"
    MatchWord(s)
    MatchWord(s1)