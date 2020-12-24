#Open a csv file
import csv 
file = open('export_orig.numbers','rb')
file_read = csv.reader(file)
data_lines = list(file_read)
print (data_lines)