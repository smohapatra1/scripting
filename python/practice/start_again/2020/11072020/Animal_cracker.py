#ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False
def animal(a,b):
    if a[0] == b [0]:
        print (True)
    else:
        print (False)
animal("Tiger","Tap")

#Method2
def animal2(text):
    word=text.upper().split()
    print (word)
    return word[0][0] == word[1][0]
animal2('Lama Lunar')