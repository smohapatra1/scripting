#   https://www.geeksforgeeks.org/python-program-to-check-if-a-string-has-at-least-one-letter-and-one-number/

# Initialize Flags
# Validate using isalpha for letter 
# Validate using isdigits for number 
# Now perform AND for both of them 

def FindLetterNum(s):
    num = False
    let = False 
    for i in s:
        if i.isalpha():
            let = True
        if i.isdigit():
            num = True
    return let and num

if __name__ == "__main__":
    # s = 'welcome2ourcountry34'
    s = 'stringwithoutnum'
    result = FindLetterNum(s)
    print (result)