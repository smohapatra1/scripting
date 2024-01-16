# #   https://www.hackerrank.com/challenges/whats-your-name/problem?isFullScreen=true


# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# Hello firstname lastname! You just delved into python.
# Function Description
# Complete the print_full_name function in the editor below.
# print_full_name has the following parameters:
# string first: the first name
# string last: the last name
# Prints
# string: 'Hello  ! You just delved into python' where  and are replaced with  and .
# Input Format
# The first line contains the first name, and the second line contains the last name.
# Constraints
# The length of the first and last names are each ≤ .
# Sample Input 0
# Ross
# Taylor
# Sample Output 0
# Hello Ross Taylor! You just delved into python.
# Explanation 0
# The input read by the program is stored as a string data type. A string is a collection of characters.


def Name(last: str, first: str) -> str:
    return first  +   last 

if __name__ == "__main__":
    last=input()
    first=input()
    print ("Hello {}! You just delved into Python".format(Name(last, first)))