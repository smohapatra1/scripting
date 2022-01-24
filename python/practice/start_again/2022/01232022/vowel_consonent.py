#Ask a letter from the user. Find out if it is a vowel or consonent.
def vowel_consonent(a):
    if type(a) != int:
        if a != 'a' and a != 'e' and a != 'i' and a != 'o' and a != 'u':
            print (f'{a} is consonent')
        else:
            print (f'{a} is vowel')
vowel_consonent(input("Enter the letter : "))
