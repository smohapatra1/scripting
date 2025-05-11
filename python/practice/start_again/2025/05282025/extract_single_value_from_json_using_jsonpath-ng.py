#   https://www.geeksforgeeks.org/python-program-to-extract-a-single-value-from-json-response/

import urllib.parse
import requests
from jsonpath_ng import jsonpath, parse

baseUrl = "https://v6.exchangerate-api.com/v6/0f215802f0c83392e64ee40d/pair/"
first = input("Enter first currency value : ")
second = input("Enter second currency value : ")
result = first + "/" + second
final_url = baseUrl + result
json_data = requests.get(final_url).json()
jsonpath_expr = parse('$.conversion_rate')
result = jsonpath_expr.find(json_data)[0].value
print("Conversion rate from " + first + " to " + second + " = ", result)
