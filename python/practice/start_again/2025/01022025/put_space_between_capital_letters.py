#   https://www.geeksforgeeks.org/regex-in-python-to-put-spaces-between-words-starting-with-capital-letters/

def AddSpace(s):
    regex = re.findall('[A-Z][a-z]*', s)
    for i in range(0, len(regex)):
        regex[i]=regex[i][0].lower()+regex[i][1:]
    print(' '.join(regex)) 
        

if __name__ == "__main__":
    s = "BruceWayneIsBatman"
    AddSpace(s)