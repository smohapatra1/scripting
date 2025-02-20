#   https://www.geeksforgeeks.org/how-to-read-specific-lines-from-a-file-in-python/
import linecache

line = linecache.getline('file.txt', 4)
print (line)