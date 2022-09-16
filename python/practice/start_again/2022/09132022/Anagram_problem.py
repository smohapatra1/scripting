#Construct an algorithm to check whether two words or phrases are anagrams or not!
#A anagram is a word or phrase formed by rearranging the letters of a different word or phase. 
# e.g. = restful - > fluster 


from xml.dom.expatbuilder import FragmentBuilderNS


def is_anagram(a,b):
    if len(a) != len(b):
        return False
    a=sorted(a)
    b=sorted(b)
    for i in range (len(a)):
        if a[i] != b[i]:
            print (f"{a} and {b} are not anagram ")
            #return False
    print (f"{a} and {b} are anagram ")
    #return True 


if __name__ == '__main__':
    a = ['r', 'e', 's', 't', 'f','u','l']
    b= ['f', 'l', 'u', 's', 't','e','x']
    is_anagram(a,b)
