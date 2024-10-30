#   https://www.geeksforgeeks.org/python-counter-find-size-largest-subset-anagram-words/

from collections import Counter

def MaxAnagramSize(input):

    # SOLUTION - 01 
    input = input.split(' ')
    for i in range(0, len(input)):
        input[i] = ''.join(sorted(input[i]))
    freq = Counter(input)
    return max(freq.values())

    # Solution -02 

    # dict = {}
    # for word in input:
    #     sorted_word = ''.join(sorted(word))
    #     if sorted_word not in dict:
    #         dict[sorted_word] = []
    #     dict[sorted_word].append(word)
    # max_count = max([len(val) for val in dict.values()])
    # return max_count

if __name__ == "__main__":
    # Input for solution - 01 
    input = 'ant magenta magnate tan gnamate'
    
    # Input for Solution  - 02 

    # input = ['ant', 'magenta', 'magnate', 'tan', 'gnamate']
    print ("Max Anagram count: ", MaxAnagramSize(input))