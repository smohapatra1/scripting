#   https://www.geeksforgeeks.org/saving-text-json-and-csv-to-a-file-in-python/

with open('read.txt', 'w') as file:
    
    books = ['Welcome\n', 
             'Geeks\n', 
             'to\n', 
             'Geeks\n',
             'for\n', 
             'Geeks\n', 
             'world\n']
    
    file.writelines("% s\n" % data for data in books)