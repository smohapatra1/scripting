#   https://www.geeksforgeeks.org/python/iterate-through-nested-json-object-using-python/

def iterative_nested_json_recursive(json_obj):
    for key, value in json_obj.items():
        if isinstance(value, dict):
            iterative_nested_json_recursive(value)
        else:
            print (f"{key}: {value}")
nested_json = {
    "name" : "sam", 
    "age" : "30",
    "address" : 
      {
          "city" : "bc",
          "zip" : "90123"
    }
}

print ("\n Using recursive Function")
iterative_nested_json_recursive(nested_json)
