#   https://www.geeksforgeeks.org/python/convert-json-to-geojson-python/

import json
import geojson

def convert_json_to_geojson(json_data):
    parsed = json.loads(json_data)
    feature = geojson.Feature(geometry=parsed["geometry"], properties=parsed["properties"])
    feature_collection = geojson.FeatureCollection([feature])
    return feature_collection

example_json_data = '''
{
  "type": "Feature",
  "properties": 
  {
    "name": "Example Feature"
  },
  "geometry": 
  {
    "type": "Point",
    "coordinates": [0, 0]
  }
}
'''
geojson_result = convert_json_to_geojson(example_json_data)
print (geojson.dumps(geojson_result, indent=2))