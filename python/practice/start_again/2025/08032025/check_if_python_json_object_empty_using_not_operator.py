#   https://www.geeksforgeeks.org/python/check-if-python-json-object-is-empty/

Test = {}
gfg = [('name', 'Sam'), ('age', 29), ('is_student', True)]

if not Test:
    print ("JSON Object 1 is Empty")
else:
    print ("JSON Object 1 is not Empty")
if not gfg:
    print ("JSON Object 2 is Empty")
else:
    print ("JSON Object 2 is not Empty")