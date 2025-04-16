#   https://www.geeksforgeeks.org/how-to-sort-column-in-a-file-using-python/

def my_sort(line):
    line_fields =  line.strip().split(',')
    amount = float(line_fields[2])
    return amount
fp = open('file.txt')
contents = fp.readlines()
contents.sort(key=my_sort) 
for line in contents: 
    print(line) 
fp.close() 
