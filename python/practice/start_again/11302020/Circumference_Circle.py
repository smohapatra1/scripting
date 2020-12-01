#Calculate the cicumference of circle using class
class circle():
    pi = 3.14
    def __init__ (self,radius=1):
        self.radius = radius
    #Method - Get circumference 
    def get_circumference (self):
        return 2 * self.pi * self.radius
    def get_area (self):
        return self.radius * self.radius * self.pi
my_circle = circle(30)
print ("The Value of pi is :- {}".format(my_circle.pi))
print ("The Value of radius is :- {}".format(my_circle.radius))
print ("The Circumference is :- {}".format(my_circle.get_circumference()))
print ("The Area is :- {}".format(my_circle.get_area()))
