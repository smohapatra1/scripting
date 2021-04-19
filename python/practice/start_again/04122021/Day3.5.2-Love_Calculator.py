#Love Calculator
#💪 This is a Difficult Challenge 💪
#Instructions
#You are going to write a program that tests the compatibility between two people. 
# We're going to use the super scientific method recommended by BuzzFeed.

#To work out the love score between two people:

#Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.

#This BuzzFeed article gives more details on this:

#https://www.buzzfeed.com/ariannarebolini/what-are-the-chances-your-crush-is-actually-your-true-love

#For Love Scores less than 10 or greater than 90, the message should be:

#"Your score is **x**, you go together like coke and mentos."

#For Love Scores between 40 and 50, the message should be:

#"Your score is **y**, you are alright together."

#Otherwise, the message will just be their score. e.g.:

#"Your score is **z**."

#e.g.

#name1 = "Angela Yu"

#name2 = "Jack Bauer"

#T occurs 0 times

#R occurs 1 time

#U occurs 2 times

#E occurs 2 times

#Total = 5

#L occurs 1 time

#O occurs 0 times

#V occurs 0 times

#E occurs 2 times

#Total = 3

#Love Score = 53

#Print: "Your score is 53."

#Example Input 1
#name1 = "Kanye West"
#name2 = "Kim Kardashian"

#Example Output 1
#Your score is 42, you are alright together.

#Example Input 2
#name1 = "Brad Pitt"
#name2 = "Jennifer Aniston"
#Example Output 2
#Your score is 73.
name1=input("Enter your first and Last Name: ")
name2=input("Enter your first and last Name: ")
combined_name= name1 + name2 
lowercase_string=combined_name.lower()
t = lowercase_string.count("t")
r = lowercase_string.count("r")
u = lowercase_string.count("u")
e = lowercase_string.count("e")

l = lowercase_string.count("l")
o = lowercase_string.count("o")
v = lowercase_string.count("v")
e = lowercase_string.count("e")
true=t+r+u+e
love=l+o+v+e
print (f"t = {t}, r = {r}, u = {u} e= {e} and TOTAL-true = {true}")
print (f"l = {l}, o = {o}, v = {v} e= {e} and TOTAL-love = {love}")
total=str(true) + str(love)
if int(total) <= 100 and int(total) >= 1:
    print(f"Your score is {total}, you are alright together.") 
else:
    print(f"Keep matching :)")
