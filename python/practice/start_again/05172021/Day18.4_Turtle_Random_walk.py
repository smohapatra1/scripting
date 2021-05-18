#Draw a random Walk
from turtle import Turtle, Screen
import turtle as t
import random
tim = t.Turtle()

#random Color
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r, g , b)
    return random_color


#colors = ["Red", "Green", "Blue", "yellow"]

direction = [ 0, 90, 180, 270]

tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    #tim.color(random.choice(colors))
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))
    
screen = Screen()
screen.exitonclick()


