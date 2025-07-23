#   https://www.geeksforgeeks.org/python/how-to-communicate-json-data-between-python-and-node-js/

from flask import Flask, request
import json

app = Flask(__name__)
@app.route('/arraysum', methods = ['POST'])
def sum_of_array():
    data = request.get_json()
    print (data)
    ls = data['array']
    result = sum(ls)
    return json.dumps({"result": result})

if __name__ == "__main__":
    app.run(port=5000)
