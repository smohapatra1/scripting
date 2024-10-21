#   https://www.geeksforgeeks.org/python-dictionary-find-mirror-characters-string/

def MirrorChar(input, k ):
    original = 'abcdefghijklmnopqrstuvwxyz'
    reverse = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(original,reverse))
    prefix = input[0:k-1]
    suffix = input[k-1:]
    mirror = ''
    for i in range(0, len(suffix)):
        mirror = mirror + dictChars[suffix[i]]
    return prefix + mirror

if __name__ == "__main__":
    input = 'paradox'
    k = 3
    print (" Values after finding the mirror chars :", MirrorChar(input, k ))