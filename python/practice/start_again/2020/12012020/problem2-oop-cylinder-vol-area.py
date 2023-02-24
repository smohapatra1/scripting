# Find the cylinder volume and surface area 
#Volume = pi * r * r * h
#Surface Area = 2 * pi * r * r + 2* pi * r * h 
class cylinder():
    pi = 3.14
    def __init__(self,height=1, radius = 1 ):
        self.height = height
        self.radius = radius 
    def get_volume(self):
        return ( self.pi * self.radius * self.radius * self.height)
    def get_area (self):
        return ( 2 * self.pi * self.radius * self.radius + 2 * self.pi * self.radius * self.height)
values = cylinder(2,3)

print ("Cylinder Volume = {}".format(values.get_volume()))
print ("Cylinder Surface Area = {}".format(values.get_area()))