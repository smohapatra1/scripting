#How do you print the first non-repeated character from a string

Num_of_chars=256

def getchars(string):
    count = [0] * Num_of_chars
    for i in string:
        count[ord(i)]+=1
    return count

def nonrepeat(string):
    count=getchars(string)
    index= -1
    k=0
    for i in string:
        if count[ord(i)] == 1:
            index=k
            break
        k+=1
    return index

if __name__ == '__main__':
    string="geeksforgeeks"
    index=nonrepeat(string)
    if index==1:
        print ("Either all chars are repeating in string or string is empty ")
    else:
        print ("First non repeating char is ", string[index])
