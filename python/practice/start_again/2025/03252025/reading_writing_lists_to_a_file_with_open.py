#   https://www.geeksforgeeks.org/reading-and-writing-lists-to-a-file-in-python/


my_list = ["item1", "item2", "item3", "item4"]

file = 'file.txt'

with open(file, 'w') as f:
    data_to_write = '\n'.join(my_list)
    file.write(data_to_write)
print (f'The last has been written to file  {file}.')