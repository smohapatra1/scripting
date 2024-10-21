# https://www.geeksforgeeks.org/python-counter-dictionary-intersection-example-make-string-using-deletion-rearrangement/

from collections import Counter
def MakeString(str1, str2):
    dict1 = Counter(str1)
    dict2 = Counter(str2)
    result = dict1 & dict2
    return result==dict1


if __name__ == "__main__":
    str1 = 'ABHISHEKsinGH'
    str2 = 'gfhfBHkooIHnfndSHEKsiAnG'
    if (MakeString(str1, str2) == True):
        print ("Possible")
    else:
        print ("Not Possible")