#   https://www.geeksforgeeks.org/python/how-to-communicate-json-data-between-python-and-node-js/


import requests

array = [1,2,3,4,5,6,7,8,9,10]
data = {'array': array}
res = requests.post('http://127.0.0.1:3000/arraysum', json=data) 
returned_data = res.json()
print (returned_data)
result = returned_data['result']
print ("Sum of Array from Node.Js", result)