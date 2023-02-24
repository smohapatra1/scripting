#Draw a Dashed Line 
from turtle import Turtle, Screen
import turtle as t
#Drawing Square 

# for _ in range(4):
#     t.forward(100)
#     t.right(90)
# screen = Screen()
# screen.exitonclick()
tim = t.Turtle()
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()
screen = Screen()
screen.exitonclick()    