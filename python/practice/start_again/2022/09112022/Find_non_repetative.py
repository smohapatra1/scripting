#Find non repeatative word from a string

from codecs import StreamReader
from collections import Counter

def nonrepat(string):
    for i in string:
        #get the frquency
        freq=Counter(string)
        print (f" \n Strings is {i} and count is {freq} \n ")
        if freq[i] == 1 :
            print(f"The first char is : {i}")
            break
if __name__ == '__main__':
    string="samar"
    nonrepat(string)