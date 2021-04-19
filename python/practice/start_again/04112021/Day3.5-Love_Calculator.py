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
count1=0
count2=0
count3=0
count4=0
for name in name1:
    #print (name)
    #count=0
    if name == "T" or name == "t":
        count1+=1    
    #print (f"T or t occured in {count} Times")
    #count=0
    if name == "R" or name == "r":
        count2+=1
    if name == "U" or name == "u":
        count3+=1
    if name == "E" or name == "e":
        count4+=1    
print (f"\n T or t occured in {count1} Times \n R or r occured in {count2} Times \n U or u occured in {count3} Times \n E or e occured in {count4} Times \n   ")
Total_name1=count1+count2+count3+count4
print (f"Total in name1 = {Total_name1}")
count1=0
count2=0
count3=0
count4=0
for name in name2:
    #print (name)
    #count=0
    if name == "L" or name == "l":
        count1+=1    
    #print (f"T or t occured in {count} Times")
    #count=0
    if name == "O" or name == "o":
        count2+=1
    if name == "V" or name == "v":
        count3+=1
    if name == "E" or name == "e":
        count4+=1    
print (f"\n L or l occured in {count1} Times \n O or o occured in {count2} Times \n V or v occured in {count3} Times \n E or e occured in {count4} Times \n   ")
Total_name2=count1+count2+count3+count4
print (f"Total in name2 = {Total_name2}")  
Total_Number= str(Total_name1) +  str(Total_name2)
print ("Total_Number")
if int(Total_Number) <= 100 and int(Total_Number) >= 20:
    print(f"Your score is {Total_Number}, you are alright together.") 
else:
    print(f"Keep matching :)")
        