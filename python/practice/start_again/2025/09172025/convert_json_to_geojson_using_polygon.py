#   https://www.geeksforgeeks.org/python/convert-json-to-geojson-python/

import json
import geojson
polygon_data = {"coordinates": [[(0,0), (0,1), (1,1), (1,0), (0,0)]]}
polygon_geojson = geojson.Polygon(coordinates=polygon_data["coordinates"])
print (geojson.dumps(polygon_geojson, indent=2))

