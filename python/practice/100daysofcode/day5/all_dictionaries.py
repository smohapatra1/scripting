#!/usr/bin/python
#Dictionary
x = {
"car" : "mustang",
"brand" : "ford",
"year" : "2019"
}
print ("prints all", x)
print ("prints fields", x["brand"])
for y in x :
   print ("For loop", y)
if "brand" in x:
   print ("if loop - Yes, brand is in dictionary")
x["color"] = "red"
print ("Added color" , x)
x.pop("color")
print ("Removing color" , x)
del x["year"]
print ("Delete year", x)
x.clear()
print ("Clear all", x)
