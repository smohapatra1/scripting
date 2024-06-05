# Counting the repeated numbers in a string


def  FindNumOfOccour(s):
    count = 0 
    character = "s"
    for i in s :
        if i == character:
            count +=1
    print (count)

if __name__ == "__main__":
    s = input()
    result = FindNumOfOccour(s)