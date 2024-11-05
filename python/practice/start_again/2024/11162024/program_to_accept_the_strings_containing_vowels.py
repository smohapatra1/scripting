#   https://www.geeksforgeeks.org/python-program-to-accept-the-strings-which-contains-all-vowels/

def AcceptVowels(s):
    s = s.lower()
    vowels = set("aeiou")
    s1 = set({})
    for char in s:
        if char in vowels:
            s1.add(char)
        else:
            pass
    if len(s1) == len(vowels):
        print ("Accepted")
    else:
        print ("Not Accepted")

if __name__ == "__main__":
    s = input("Enter the string : ")
    AcceptVowels(s)