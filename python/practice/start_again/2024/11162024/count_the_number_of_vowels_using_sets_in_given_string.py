#   https://www.geeksforgeeks.org/python-program-count-number-vowels-using-sets-given-string/

string = "GeekforGeeks!"
vowels = "aeiouAEIOU"
count = sum(string.count(vowel) for vowel in vowels)
print ("Number of Vowels are : ", count)