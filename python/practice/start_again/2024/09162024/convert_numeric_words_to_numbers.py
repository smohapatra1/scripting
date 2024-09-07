#   https://www.geeksforgeeks.org/python-convert-numeric-words-to-numbers/?ref=leftbar-rightbar


def convert(s):
    word_to_digit = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }
    words = s.split()
    digits = [word_to_digit[word] for word in words]
    res = ''.join(digits)
    return res


if __name__ == "__main__":
    s = "one two three four five"
    result = convert(s)
    print (result)