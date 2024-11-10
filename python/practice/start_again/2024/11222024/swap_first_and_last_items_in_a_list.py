#   https://www.geeksforgeeks.org/python-program-to-interchange-first-and-last-elements-in-a-list/
a = [12, 35, 9, 56, 24]
get = a[-1], a[0]
a[0], a[-1] = get
print (a)