#   https://www.geeksforgeeks.org/python/decoding-json-string-with-single-quotes-in-python/

import ast  

json_string = "{'name': 'Ragu','age': 30,'salary':30000,'address': { 'street': 'Gradenl','city': 'Pune','state': 'Maharastra'}}"
my_dict = ast.literal_eval(json_string)
print ("Decoding using single quotes : ")
print ("The address of %s is" % my_dict['name'], my_dict['address'])