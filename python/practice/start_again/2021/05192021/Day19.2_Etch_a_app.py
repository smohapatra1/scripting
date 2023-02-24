#Etch a Sketh App

from turtle import Turtle, Screen
import turtle as t
import random 
screen = Screen()
tim = t.Turtle()

def move_forward():
    tim.forward(100)

def move_backward():
    tim.backward(100)

def move_right():
    new_move = tim.heading() + 10 
    tim.setheading(new_move)

def move_left():
    new_move = tim.heading() - 10 
    tim.setheading(new_move)
    
def clear():
    tim.clear()
    tim.home()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(clear, "c")
screen.exitonclick()
