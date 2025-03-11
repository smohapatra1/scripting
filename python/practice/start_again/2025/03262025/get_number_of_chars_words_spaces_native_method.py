#   https://www.geeksforgeeks.org/python-get-number-of-characters-words-spaces-and-lines-in-a-file/

def Counter(fname):
    num_words = 0 
    num_chars = 0 
    num_space = 0 
    num_lines = 0 
    with open(fname, 'r') as f:
        for line in f:
            num_lines += 1
            word = 'Y'
            for letter in line:
                if (letter != ' ' and word == 'Y'):
                    num_words += 1 
                    word = 'N'
                elif (letter == ' '):
                    num_space += 1
                    word = 'Y'
            for i in letter:
                if (i != ' ' and i != '\n'):
                    num_chars += 1
    print('Number of words in text file :', num_words)
    print('Number of characters in text file :', num_chars)
    print('Number of spaces in text file :', num_space)
    print('Number of lines in text file :', num_lines)
if __name__ == '__main__':
    fname = 'file.txt'
    try:
        Counter(fname)
    except:
        print('File not found')
