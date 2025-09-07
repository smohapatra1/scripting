#   https://www.geeksforgeeks.org/python/saving-api-result-into-json-file-in-python/

from fastapi import FastAPI
import json
app = FastAPI()
@app.get("/Hello-world")

def hello():
    data = {
    "message:" "Hello, world"
    "details":{
        "author":{
            "name": "sam",
            "email": "xyz@gmail.com"

        },
        "tags": ["fastapi", "python", "web"]
        }
    }
    return data