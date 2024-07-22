# #   https://www.hackerrank.com/challenges/password-cracker/problem?isFullScreen=true

# There are n users registered on a website CuteKittens.com. Each of them has a unique password represented by pass[1], pass[2], ..., pass[N]. As this a very lovely site, many people want to access those awesomely cute pics of the kittens. But the adamant admin does not want the site to be available to the general public, so only those people who have passwords can access it.

# Yu, being an awesome hacker finds a loophole in the password verification system. A string which is a concatenation of one or more passwords, in any order, is also accepted by the password verification system. Any password can appear  or more times in that string. Given access to each of the  passwords, and also have a string , determine whether this string be accepted by the password verification system of the website. If all of the  string can be created by concatenating password strings, it is accepted. In this case, return the passwords in the order they must be concatenated, each separated by a single space on one line. If the password attempt will not be accepted, return 'WRONG PWASSWORD'.

# Examples


# Concatenate the passwords in index order  to match 'abrakadabra'. Return 'abra ka dabra'.



# Concatenate the passwords in index order  to match 'kaabra'. Return 'ka abra'.



# Concatenate the passwords in index order  to match 'abba',  to match 'baab',  to match 'abab' or  to match $baba'. No combination of 1 or more passwords can be concatenated to match 'aba'. Return 'WRONG PASSWORD'.

# Function Description

# Complete the passwordCracker function in the editor below.

# passwordCracker has the following parameters:
# - string passwords[n]: a list of password strings
# - string loginAttempt: the string to attempt to create

# Returns
# - string: Return the passwords as a single string in the order required for the password to be accepted, each separated by a space. If it is not possible to form the string, return the string WRONG PASSWORD.

# Input Format

# The first line contains an integer t, the total number of test cases.

# Each of the next  sets of three lines is as follows:
# - The first line of each test case contains n, the number of users with passwords.
# - The second line contains n space-separated strings, passwords[i], that represent the passwords of each user.
# - The third line contains a string, loginAttempt, which Yu must test for acceptance.

# Constraints

# , where 
# loginAttempt and passwords[i] contain only lowercase latin characters ('a'-'z').
# Sample Input 0

# 3
# 6
# because can do must we what
# wedowhatwemustbecausewecan
# 2
# hello planet
# helloworld
# 3
# ab abcd cd
# abcd
# Sample Output 0

# we do what we must because we can
# WRONG PASSWORD
# ab cd
# Explanation 0

# Sample Case #00: "wedowhatwemustbecausewecan" is the concatenation of passwords {"we", "do", "what", "we", "must", "because", "we", "can"}. That is

# loginAttempt = pass[5] + pass[3] + pass[6] + pass[5] +  pass[4] + pass[1] + pass[5] + pass[2]
# Note that any password can repeat any number of times.

# Sample Case #01: We can't create string "helloworld" using the strings {"hello", "planet"}.

# Sample Case #02: There are two ways to create loginAttempt ("abcd"). Both pass[2] = "abcd" and pass[1] + pass[3] = "ab cd" are valid answers.

# Sample Input 1

# 3
# 4
# ozkxyhkcst xvglh hpdnb zfzahm
# zfzahm
# 4
# gurwgrb maqz holpkhqx aowypvopu
# gurwgrb
# 10
# a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa
# aaaaaaaaaab
# Sample Output 1

# zfzahm
# gurwgrb
# WRONG PASSWORD

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'passwordCracker' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING_ARRAY passwords
#  2. STRING loginAttempt
#

T = int(input())
for t in range(T):
   N = int(input())
   pwd = input().split()
   login = input().strip()
   a = [None] * (len(login) + 1)
   a[0] = []
   for i in range(len(login)):
      if a[i] == None: continue
      for p in pwd:
         j = i + len(p)
         if j < len(a) and a[j] == None and login[i:j] == p:
            a[j] = a[i] + [p]
   if a[-1] == None:
      print('WRONG PASSWORD')
   else:
      print(' '.join(a[-1]))

# def passwordCracker(passwords, loginAttempt):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         n = int(input().strip())

#         passwords = input().rstrip().split()

#         loginAttempt = input()

#         result = passwordCracker(passwords, loginAttempt)

#         fptr.write(result + '\n')

#     fptr.close()
