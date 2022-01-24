#Draw Polygon using turtle
import turtle
#t=turtle.Turtle
#turtle.resetscreen()
def polygon(distance,n):
    angle=int(360/n)
    for i in range(n):
        turtle.fd(turtle.distance)
        turtle.lt(60)
turtle.mainloop()        
polygon(100,6)        
