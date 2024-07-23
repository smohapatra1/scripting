# Find the number of Vowels and Consonants in a string 

def FindVowelsConsonants(t):
    
    v_count = 0
    c_count = 0 
    v = ('a', 'e', 'i', 'o', 'u')
    for i in range(0, len(t)):
        if t[i] in v :
            v_count = v_count +1 
        elif t[i] >= 'a' and t[i] <= 'z' :
            c_count = c_count +1 
    print ("Total Vowels are {} and Total Consonants are {}".format(v_count, c_count))

if __name__ == "__main__":
    t = input("Enter the string: ")
    result = FindVowelsConsonants(t)