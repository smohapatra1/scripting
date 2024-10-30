#   https://www.geeksforgeeks.org/print-anagrams-together-python-using-list-dictionary/

def Anagram(input):
    dict = {}
    for val in input:
        key = ''.join(sorted(val))
        if key in dict.keys():
            dict[key].append(val)
        else:
            dict[key] = []
            dict[key].append(val)
    output = ''
    for key, value in dict.items():
        output = output + ' '.join(value) + ' '
    return output

if __name__ == "__main__":
    input=['cat', 'dog', 'tac', 'god', 'act']
    print ("Anagram values ", Anagram(input))