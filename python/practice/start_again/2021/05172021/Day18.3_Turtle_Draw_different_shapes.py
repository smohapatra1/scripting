#Draw different shapes and with 100 spaces with different color 
from turtle import Turtle, Screen
import turtle as t
import random

colors = [ "indigo", "lime green", "royal blue", "khaki", "chartreuse", "red", "green", "orange", "magneta", "dark violet"]
# Square 
tim = t.Turtle()
def draw_sides(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        #tim.color("Red")
        tim.forward(100)
        tim.right(angle)
        

for shape_side_n in range(5,11):
    tim.color(random.choice(colors))
    draw_sides(shape_side_n)

screen= Screen()
screen.exitonclick()