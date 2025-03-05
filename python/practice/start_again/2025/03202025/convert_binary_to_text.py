#   https://www.geeksforgeeks.org/reading-binary-files-in-python/

with open('example.bin', 'rb') as f :
    binary_data = f.read()
    print ('\n',  binary_data , '\n')
    text_data = binary_data.decode('utf-8')
    print ('\n', text_data, '\n')