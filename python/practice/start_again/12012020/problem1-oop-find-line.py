#Fill in the Line class methods to accept coordinates as a pair of tuples 
#and return the slope and distance of the line.
# Distance = squareroot of [( x2 - x1)**2 + (y2 -y1)**2 ]
# Slope = (y2 - y1)/(x2 - x1)
class line(object):
    def __init__(self,cord1,cord2):
        self.cord1 = cord1
        self.cord2 = cord2

    def get_distance(self):
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    def get_slope(self):
        x1,y1 = self.cord1
        x2,y2 = self.cord2
        return (y2 - y1)/(x2 - x1)
coordinate1 = (3,2)
coordinate2 = (8,10)
values = line(coordinate1, coordinate2)
print (values.get_distance())
print (values.get_slope())