#Enter the sentence. Count the occurance of each letter at their place

def count_occurance(a):
    count=0
    for letter in a:
        b=a.count(letter)
        print (f"word - {a} and count - {count} letter - {letter} - times  {b}")
        count+=1
count_occurance(str(input("Enter the word: ")))