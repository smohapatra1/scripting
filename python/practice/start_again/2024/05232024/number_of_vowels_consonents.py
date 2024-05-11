#   How do you calculate the number of vowels and consonants in a String?


def Vowels_Consonants(n):
    vCount = 0 
    cCount = 0 
    v = n.lower()
    for i in range(len(n)):
        if n[i] in ('a', 'e', 'i', 'o', 'u'):
            vCount +=1
        elif ( n[i] >= 'a' and n[i] <= 'z'):
            cCount +=1
    print ("Number of Vowels in  string    {} are : {}".format(n, vCount))
    print ("Number of Consonants in string {} are : {}".format(n, cCount))

if __name__ == "__main__":
    n = input()
    result = Vowels_Consonants(n)
    #print (result)