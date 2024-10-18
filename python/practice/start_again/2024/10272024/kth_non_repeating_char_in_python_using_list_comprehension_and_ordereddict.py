#   https://www.geeksforgeeks.org/kth-non-repeating-character-python-using-list-comprehension-ordereddict/

from collections import OrderedDict
def KthRepeatingChar(input, k ):
    dict = OrderedDict.fromkeys(input, 0 )
    for char in input:
        dict[char] +=1
    nonRepeatingDict=[key for (key, value) in dict.items() if value == 1]
    if len(nonRepeatingDict) < k:
        return 'Less than k non-repeating chars in input'
    else:
        return nonRepeatingDict[k-1]
    return nonRepeatingDict

if __name__ == "__main__":
    input = "geeksforgeeks"
    k = 3
    print (KthRepeatingChar(input, k))