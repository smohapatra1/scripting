#   https://www.geeksforgeeks.org/python-check-url-string/

import re

def Find(string):
    x = string.split(' ')
    res = []
    for i in x:
        if i.startswith('https:') or i.startswith('http:'):
            res.append(i)
    return res


if __name__ == "__main__":
    string = 'My Profile: https://auth.geeksforgeeks.org/user/Chinmoy%20Lenka/articles in the portal of https://www.geeksforgeeks.org/'
    print ("URLS ", Find(string))