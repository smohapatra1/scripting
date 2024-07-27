# How Do You Determine Whether the Following Two Strings Are Anagrams of Each Other?

def anagram(a,b):
    if len(a) == len(b):
        if sorted(a) == sorted (b):
            return 'YES'
    return 'NO'

if __name__ == "__main__":
    a = input("Enter string A: ")
    b = input("Enter string B: ")
    result = anagram(a,b)
    print (result)