#Working with PDF, CSV and Excel file 
import csv
import codecs
data = open('On-call_2020_Holiday.csv',encoding='utf-8')
read_data = csv.reader(data)
all_data = list(read_data)
print (all_data)