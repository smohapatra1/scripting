#   https://www.geeksforgeeks.org/write-multiple-variables-to-a-file-using-python/

n = 'test'
a = 2009
p = True
with open('file.txt', 'w') as f:
    f.write('website_name= ' + repr(n) + '\n')
    f.write('funded_year = ' + repr(a) + '\n')
    f.write('is_popular  = ' + repr(p) + '\n')

print (f.readlines)

