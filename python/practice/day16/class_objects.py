#!/usr/bin/python
#Class
class vehicle:
    speed = 0
#Creating Instance    
    def Increasedspeed(self,increaseAmount):
        self.speed +=increaseAmount
#Acessing Attributes        
car1 = vehicle()
car2 = vehicle()
print ("Car speed = %d" % car1.speed)
car1.Increasedspeed(5)
print ("Car speed = %d" % car1.speed)
print ("Car speed = %d" % car2.speed)

