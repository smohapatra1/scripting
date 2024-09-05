#   https://www.geeksforgeeks.org/python-find-close-matches-input-string-list/


from difflib import get_close_matches

def CloseMatches(word, patters):
    print (get_close_matches(word, patterns))

if __name__ == "__main__":
    word = 'appel'
    patterns = ['ape', 'apple', 'peach', 'puppy']
    result = CloseMatches(word, patterns)