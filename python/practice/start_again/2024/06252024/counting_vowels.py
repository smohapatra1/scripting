# Counting vowels in a string

def VowelsCount(s):
    count = 0 
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in s:
        if i in vowels: 
            count +=1
    return count


if __name__ == "__main__":
    s = input()
    result=VowelsCount(s)
    print (result)

