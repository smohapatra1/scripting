#   https://www.geeksforgeeks.org/python/convert-nested-json-to-csv-in-python/

import json
import pandas

def read_json(filename : str) -> dict:
    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        # print ("Error")
        raise Exception(f"Reading {filename} file encountered an error")

    return data

def normalize_json(data: dict) -> dict:
    new_data = dict()
    for key, value in data.items():
        if not isinstance(value, dict):
            new_data[key] = value
        else:
            for k, v in value.items():
                new_data[key + "_" + k ] = v
    return new_data

def main():
    data = read_json(filename="samaple.json")
    new_data = normalize_json(data = data)
    print ("New Dict:", new_data, "\n")
    dataframe = pandas.DataFrame(new_data, index=[0])
    dataframe.to_csv("test.csv")


if __name__ == "__main__":
    main()