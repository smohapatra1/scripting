#   https://www.geeksforgeeks.org/eliminating-repeated-lines-from-a-file-using-python/

f1 = open('file.txt', 'w')
f2 = open('file2.txt','r')
lines_seen = set()
for line in f2:
    if line not in lines_seen:
        f1.write(line)
        lines_seen.add(line)
f1.close()
f2.close()