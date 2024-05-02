# #   https://www.hackerrank.com/challenges/palindromic-border/problem?isFullScreen=true

# A border of a string is a proper prefix of it that is also a suffix. For example:

# a and abra are borders of abracadabra,
# kan and kankan are borders of kankankan.
# de is a border of decode.
# Note that decode is not a border of decode because it's not proper.

# A palindromic border is a border that is palindromic. For example,

# a and ana are palindromic borders of anabanana,
# l, lol and lolol are palindromic borders of lololol.
# Let's define  as the number of palindromic borders of string . For example, if  lololol, then .

# Now, a string of length  has exactly  non-empty substrings (we count substrings as distinct if they are of different lengths or are in different positions, even if they are the same string). Given a string , consisting only of the first 8 lowercase letters of the English alphabet, your task is to find the sum of  for all the non-empty substrings  of . In other words, you need to find:

# where  is the substring of  starting at position  and ending at position .
# Since the answer can be very large, output the answer modulo .

# Input Format

# The first line contains a string consisting of  characters.

# Output Format

# Print a single integer: the remainder of the division of the resulting number by .

# Constraints


# All characters in the string can be any of the first 8 lowercase letters of the English alphabet (abcdefgh).

# Sample Input 1

# ababa
# Sample Output 1

# 5
# Sample Input 2

# aaaa
# Sample Output 2

# 10
# Sample Input 3

# abcacb
# Sample Output 3

# 3
# Explanation

#  ababa has 15 substrings but only 4 substrings have palindromic borders.

#  aba 
#  ababa 
#  bab 
#  aba 


def is_palin(s):
    head, tail = 0, len(s) - 1
    while head < tail:
        if s[head] != s[tail]:
            return False
        head += 1
        tail -= 1
    return True

#key is a palin, value is the times it appears
def calc_palin_borders(palin_dict):
    #print('palin_dict= ', palin_dict)
    output = 0
    for palin, times in palin_dict.items():
        output += times * (times - 1) // 2
    return output

def mono_str(s):
    cc = s[0]
    for c in s:
        if c != cc:
            return False
    return True

def mono_str_result(s):
    output = 0
    for i in range(2, len(s) + 1):
        output += i * (i - 1) // 2
        output %= 1000000007
    return output

def pb(s):
    if mono_str(s):
        return mono_str_result(s)
    output = 0

    #palin tuple for substring of length 1
    odd = [[], {}, 1]
    for c in s:
        if c not in odd[1]:
            odd[1][c] = 0
        odd[1][c] += 1
    for i in range(len(s)):
        odd[0].append(i)
    output += calc_palin_borders(odd[1])
    #print('odd = ', odd)

    #palin tuple for substring of length 2
    even = [[], {}, 1]
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            even[0].append(i)
            ss = s[i:i + 2]
            if ss not in even[1]:
                even[1][ss] = 0
            even[1][ss] += 1
    output += calc_palin_borders(even[1])
    #print('even = ', even)

    for l in range(3, len(s)):
        #print('l = ', l)
        #working tuple
        if l % 2 == 0:
            wt = even
        else:
            wt = odd

        new_tuple = [[], {}, l] 
        for idx in wt[0]:
            if idx - 1 >= 0 and idx + l - 2 < len(s) and s[idx - 1] == s[idx + l - 2]:
                new_tuple[0].append(idx - 1)
                ss = s[idx - 1:idx - 1 + l]
                if ss not in new_tuple[1]:
                    new_tuple[1][ss] = 0
                new_tuple[1][ss] += 1

        #print('new_tuple= ', new_tuple)
        output += calc_palin_borders(new_tuple[1])
        output %= 1000000007
        if l % 2 == 0:
            even = new_tuple
        else:
            odd = new_tuple
    return output

if __name__ == '__main__':
    print(pb(input()))