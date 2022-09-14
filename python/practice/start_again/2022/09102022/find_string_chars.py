#Program to count occurrence of a given character in a string

def Find_String(a, c):
    counter=0
    for i in a:
        if i == c:
            counter+=1
    print (f"The {c} existed in {counter} times")

if __name__ == '__main__':
    Find_String(str(input("Enter the string: ")), str(input("Enter the char: ")))
