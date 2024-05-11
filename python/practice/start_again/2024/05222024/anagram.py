#   How to find out if the given two strings are anagrams or not?


def Anagrams(n1, n2):
    if len(n1) == len(n2):
        if sorted(n1) == sorted(n2):
            return 'YES'
    return 'NO'

if __name__ == "__main__":
    n1 = input()
    n2 = input()
    result = Anagrams(n1, n2)
    print (result)
