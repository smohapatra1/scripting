#   https://www.geeksforgeeks.org/ways-sort-list-dictionaries-values-python-using-lambda-function/
data_list = [{"name": "Nandini", "age": 20},
       {"name": "Manjeet", "age": 20},
       {"name": "Nikhil", "age": 19}]
print ("Getting sorted list by age")
print (sorted(data_list, key=lambda i:i['age']))
print ('\r')
print ("Getting sorted list by age and name ")
print (sorted(data_list, key=lambda i : (i['age'], i['name'])))
print ('\r')
print ("Getting sorted list by age by reverse order  ")
print (sorted(data_list, key=lambda i : i['age'], reverse=True))
print ('\r')