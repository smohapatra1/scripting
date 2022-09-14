#How do you convert a given String into int like the atoi()?
#https://codeburst.io/100-coding-interview-questions-for-programmers-b1cf74885fb7

#Coverting a string to an integer 

def myatoi(string):
    res=0
    for i in range (len(string)):
        res=res * 10 + ord(string[i]) * ord('0')
    return res
if __name__ == '__main__':
    string="10"
    myatoi(string)
    print (myatoi(string))