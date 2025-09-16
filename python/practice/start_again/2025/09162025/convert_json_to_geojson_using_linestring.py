#   https://www.geeksforgeeks.org/python/convert-json-to-geojson-python/

import geojson
linestring_data = {"coordinates": [(0, 0), (1, 1), (2, 2)]}
linestring_geojson = geojson.LineString(coordinates=linestring_data["coordinates"])
feature_collection = geojson.FeatureCollection(features=[geojson.Feature(geometry=linestring_geojson)])
print (geojson.dumps(feature_collection, indent=2))