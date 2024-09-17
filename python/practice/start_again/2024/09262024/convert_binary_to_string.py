#   https://www.geeksforgeeks.org/convert-binary-to-string-using-python/

def Convert_bin_to_str(bin_data):
    string = int(bin_data, 2)
    return string
bin_data ='10001111100101110010111010111110011'
str_data = ' '
for i in range(0, len(bin_data), 7 ):
    temp_data = bin_data[i:i +7]
    decimal_data = Convert_bin_to_str(temp_data)
    str_data = str_data + chr(decimal_data)
print ("The new string is {}".format(str_data))
