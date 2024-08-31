#   https://www.geeksforgeeks.org/python-program-count-number-vowels-using-sets-given-string/

def CountVowels(string, vowels):
    count = sum(string.count(vowel) for vowel in vowels)
    return count

if __name__ == "__main__":
    string = "GeekforGeeks!"
    vowels = "aeiouAEIOU"
    result = CountVowels(string, vowels)
    print (result)
