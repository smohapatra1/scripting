#   https://www.geeksforgeeks.org/python-program-to-count-the-number-of-occurrences-of-a-key-value-pair-in-a-text-file/

f = open('file.txt', 'r')
d = dict()
for res in f:
    res = res.lower()
    lines = res.split()
    for line in lines:
        if line in d:
            d[line] = d[line]+1
        else:
            d[line] = 1 
f.close()
for key in list(d.keys()):
    print ("the count of {} is {}".format(key,d[key]))