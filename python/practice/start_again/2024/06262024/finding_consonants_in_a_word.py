# Finding a consonants in a string 

def FindConsonants(s):
    count = 0 
    vowels = ['a','e','i','o','u']
    for i in s:
        if i not in vowels:
            count +=1
    print (count)



if __name__ == "__main__":
    s = input()
    result = FindConsonants(s)