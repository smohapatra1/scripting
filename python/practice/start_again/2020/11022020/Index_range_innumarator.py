index=0
for i in 'abcd':
    print ("The index is {} and the letter is {} ".format(index, i))
    index +=1

#OR another way 
index=0
word = "abcd"
for i in word:
    print (word[index])
    index +=1