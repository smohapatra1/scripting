#   https://www.hackerrank.com/test/3fmlgi1ase7/questions/bae9p3effgk

from collections import Counter

def anagram(s):
    if len(s) % 2 !=0:
        return 1
    return sum((Counter(s[:len(s)//2])- Counter(s[len(s)//2:])).values())



if __name__ == "__main__":
    a=int(input().strip())
    for a_itr in range(a):
        s=input()
        result=anagram(s)
        print (result)