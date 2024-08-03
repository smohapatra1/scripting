#   Compare two strings anagrams


def Anagram(str1, str2):
    str1 = list(str1.upper())
    str2 = list(str2.upper())
    str1.sort(), str2.sort()
    if str1 == str2:
        return 'True'
    else:
        return 'False'

if __name__ == "__main__":
    str1 = "Listen"
    str2 = "Silent"
    result = Anagram(str1, str2)
    print (result)