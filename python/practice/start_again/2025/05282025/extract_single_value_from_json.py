#   https://www.geeksforgeeks.org/python-program-to-extract-a-single-value-from-json-response/

import urllib.parse
import json
import requests

baseurl = "https://v6.exchangerate-api.com/v6/0f215802f0c83392e64ee40d/pair/"

first = input("Enter First currency Value")
second = input("Enter Second current Value")

result = first + "/" + second
final_url = baseurl + result

json_data = requests.get(final_url).json()
final_result = json_data["conversion_rate"]

print ("Conversion rate from "+first+" to "+second+" = ", final_result)
