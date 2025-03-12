#   https://www.geeksforgeeks.org/python-get-number-of-characters-words-spaces-and-lines-in-a-file/

import os 

def Counter(fname):
    num_words = 0 
    num_lines = 0 
    num_spaces = 0 
    num_chars = 0 
    with open(fname, 'r') as f :
        for line in f:
            line = line.strip(os.linesep)
            wordlist = line.split()
            num_lines = num_lines + 1
            num_words = num_words + len(wordlist)
            num_chars = num_chars + sum(1 for c in line if c not in (os.linesep, ' '))
            num_spaces = num_spaces + sum(1 for s in line if s in (os.linesep, ' '))
    print ("Number of words in text file : ", num_words)
    print ("Number of lines in text file : ", num_lines)
    print ("Number of chars in text file : ", num_chars)
    print ("Number of spaces in text file : ", num_spaces)
if __name__ == '__main__':
    fname = 'file.txt'
    try:
        Counter(fname)
    except: 
        print ("File not found")
