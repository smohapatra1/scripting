#   https://www.geeksforgeeks.org/how-to-create-a-list-of-object-in-python-class/

class Test:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll
list = []
list.append(Test('Sam', 2))
list.append(Test('Age', 20))
list.append(Test('Home', 40))
for obj in list:
    print (obj.name, obj.roll, sep=' ')
print ("")
print (list[0].name)
print (list[1].name)
print (list[2].name)