#   https://www.geeksforgeeks.org/python/convert-nested-json-to-csv-in-python/

import json

def read_json(filename: str) -> dict:
    try:
        with open(filename, "r") as f:
            data = json.loads(f.read())
    except:
        raise Exception(f"Reading {filename} file encountered an error")

    return data

def normalize_json(data: dict) -> dict:
    new_data = dict()
    for key, value in data.items():
        if not isinstance(value, dict):
            new_data[key] = value
        else:
            for k, v in value.items():
                new_data[key + "_" + k] = v

    return new_data

def generate_csv_data(data: dict) -> str:
    csv_columns = data.keys()
    csv_data = ",".join(csv_columns) + "\n"
    new_row = list()
    for col in csv_columns:
        new_row.append(str(data[col]))
    csv_data += ",".join(new_row) + "\n"

    return csv_data

def write_to_file(data: str, filepath: str) -> bool:
    try:
        with open(filepath, "w+") as f:
            f.write(data)
    except:
        raise Exception(f"Saving data to {filepath} encountered an error")

def main():
    data = read_json(filename="file.txt")
    new_data = normalize_json(data=data)
    print ("new dict: ", new_data)
    csv_data = generate_csv_data(data=new_data)
    write_to_file(data=csv_data, filepath="data.csv")
if __name__ == '__main__':
    main()
