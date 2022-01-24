#Draw a square using turtle module 
import turtle
#t=turtle.Turtle()
turtle.resetscreen()
def square(distance):
    for i in range(4):
        turtle.fd(distance)
        turtle.lt(90)

#turtle.mainloop() 
#t.clear()      
square(100)