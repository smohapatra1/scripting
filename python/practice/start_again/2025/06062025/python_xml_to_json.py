#   https://www.geeksforgeeks.org/python-xml-to-json/

import json
import xmltodict
with open("file.xml") as f:
    data_dict = xmltodict.parse(f.read())
    json_data = json.dumps(data_dict)
    with open("data.json", "w") as json_file:
        json_file.write(json_data)
        # json_file.close()