# #   https://www.hackerrank.com/challenges/one-month-preparation-kit-sparse-arrays/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-month-preparation-kit&playlist_slugs%5B%5D=one-month-week-one
# There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.

# Example



# There are  instances of ',  of '' and  of ''. For each query, add an element to the return array, .

# Function Description

# Complete the function matchingStrings in the editor below. The function must return an array of integers representing the frequency of occurrence of each query string in strings.

# matchingStrings has the following parameters:

# string strings[n] - an array of strings to search
# string queries[q] - an array of query strings
# Returns

# int[q]: an array of results for each query
# Input Format

# The first line contains and integer , the size of .
# Each of the next  lines contains a string .
# The next line contains , the size of .
# Each of the next  lines contains a string .

# Constraints



#  .

# Sample Input 1

# CopyDownload
# 4
# aba
# baba
# aba
# xzxb
# 3
# aba
# xzxb
# ab
# Sample Output 1

# 2
# 1
# 0

# Sample Input 2

# CopyDownload
# 3
# def
# de
# fgh
# 3
# de
# lmn
# fgh
# Sample Output 2

# 1
# 0
# 1

# Sample Input 3

# CopyDownload
# 13
# abcde
# sdaklfj
# asdjf
# na
# basdn
# sdaklfj
# asdjf
# na
# asdjf
# na
# basdn
# sdaklfj
# asdjf
# 5
# abcde
# sdaklfj
# asdjf
# na
# basdn
# Sample Output 3

# 1
# 3
# 4
# 3
# 2



def matchingStrings(strings, queries):
    # Write your code here
    countArr= []
    for i in queries:
        count=0
        for j in strings:
            if i == j:
                count +=1
        countArr.append(count)
    return countArr

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    strings_count = int(input().strip())
    strings = []
    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)
    queries_count = int(input().strip())
    queries = []
    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)
    res = matchingStrings(strings, queries)
    print (res)

    # fptr.write('\n'.join(map(str, res)))
    # fptr.write('\n')

    # fptr.close()