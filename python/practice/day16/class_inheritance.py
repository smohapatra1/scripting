#!/usr/bin/python
#Class
class vehicle(object):
    speed = 5
#Constructor    
    def __new__ (cls):
        return object.__new__(cls)

#Initializing the class
    def __init__ (self, speed = 100):
        self.speed = speed

#Creating Instance    
    def Increasedspeed(self,increaseAmount):
        self.speed +=increaseAmount
    def __del__ (self):
        print ("Object is destroyed")
class car(vehicle):
    weight = 500
    def Increasedweight(self,weight):
        self.weight += weight
#Acessing Attributes        
car1 = vehicle()
car2 = vehicle()
childCar = car
print ("car weight is %d" % childCar.weight)

print ("Car speed = %d" % car1.speed)
car1.Increasedspeed(5)
print ("Car1 speed incrsed = %d" % car1.speed)
print ("Car2 speed incrsed= %d" % car2.speed)
del car1


