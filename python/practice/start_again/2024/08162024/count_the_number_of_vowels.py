#   Count the number of vowels in a given string.

def CountString(s):
    vowels = 'aeiou'
    return sum(1 for char in s if char in vowels )

if __name__ == "__main__":
    s = input("Enter the string")
    result = CountString(s)
    print (result)