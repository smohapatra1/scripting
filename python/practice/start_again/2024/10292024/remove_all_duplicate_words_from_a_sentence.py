#   https://www.geeksforgeeks.org/python-remove-duplicates-words-given-sentence/
from collections import Counter

def RemoveDup(input):
    print ("Current String : " + input)
    temp = input.split(' ')
    Uword = Counter(temp)
    s = ' '.join(Uword.keys())
    return s
if __name__ == "__main__":
    input = 'Python is great and Java is also great'
    print ("Sentence after removing Duplicate : ",RemoveDup(input))