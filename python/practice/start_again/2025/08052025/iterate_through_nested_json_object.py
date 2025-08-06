#   https://www.geeksforgeeks.org/python/iterate-through-nested-json-object-using-python/

def iterate_nested_json_loop(json_obj):
    for key, value in json_obj.items():
        if isinstance(value, dict):
            iterate_nested_json_loop(value)
        else:
            print (f"{key}: value")

nested_json = {
    "name" : "sam", 
    "age" : "30",
    "city" : "ba"
}
print ("Using for loop")
iterate_nested_json_loop(nested_json)