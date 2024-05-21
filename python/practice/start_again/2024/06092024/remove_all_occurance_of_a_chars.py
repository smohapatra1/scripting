#   How do you remove all occurrences of a given character from the input string?

def RemOccur(test_str, char):
    test_str.lower()
    return  test_str.replace(char, '')


if __name__ == "__main__":
    test_str = "Samarendra"
    char = 'a'
    result = RemOccur(test_str, char)
    print (result)