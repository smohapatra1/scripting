#   https://www.geeksforgeeks.org/python-program-to-build-flashcard-using-class-in-python/

class flashcard:
    def __init__ (self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__ (self):
        return self.word+' ( '+self.meaning+' )'
flash = []
print ("Welcome to flashcard application")
while(True):
    word = input("Enter the name you want to add into flashcard: ")
    meaning = input("Enter the meaning of the word: ")
    flash.append(flashcard(word, meaning))
    options = input("enter 0, if you want to add another flashcard ")
    if (options):
        break
print ("\n Your flashcards")
for i in flash:
    print (">", i )