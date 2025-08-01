#   https://www.geeksforgeeks.org/python/inventory-management-with-json-in-python/

import json

# Creating Dictionary to store data
available_products = {1001: {"name": "avocado", "price": 230,
                             "category": "grocery",
                             "quantity": 10, "date": "10/03/2021"},
                      1002: {"name": "lotion", "price": 250,
                             "category": "beauty & personal", 
                             "quantity": 100,
                             "date": "15/07/2021"},
                      1003: {"name": "pain reliever", "price": 500, 
                             "category": "health",
                             "quantity": 200, "date": "12/04/2021"},
                      1004: {"name": "dry pasta", "price": 20, 
                             "category": "grocery",
                             "quantity": 50, "date": "27/06/2021"},
                      1005: {"name": "toothbrush", "price": 700,
                             "category": "beauty & personal", 
                             "quantity": 100,
                             "date": "30/01/2021"},
                      1006: {"name": "halloween candy", "price": 33,
                             "category": "grocery",
                             "quantity": 56, "date": "22/02/2021"},
                      1007: {"name": "mascara", "price": 765,
                             "category": "beauty & personal", 
                             "quantity": 70,
                             "date": "11/03/2021"},
                      1008: {"name": "capsicum", "price": 764,
                             "category": "grocery",
                             "quantity": 90, "date": "16/02/2021"},
                      1009: {"name": "blush", "price": 87,
                             "category": "beauty & personal",
                             "quantity": 50, "date": "17/07/2021"},
                      1010: {"name": "granola bars", "price": 24,
                             "category": "grocery", "quantity": 60,
                             "date": "20/05/2021"},
                      }

js = json.dumps(available_products)
df = open("data.json", 'w')
df.write(js)
df.close()