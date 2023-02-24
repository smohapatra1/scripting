from turtle import Turtle, Screen
import random 
screen = Screen()
screen.setup(width=500, height=400)
user_bet= screen.textinput(title="Make your bet", prompt="While turtle will win")
color = ["red", "orange", "blue", "purple", "yellow", "green"]
y_position = [-70, -40, -10, 20, 50, 80 ]
all_turtle = []
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)

is_race_on=False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print (f"You have own. The winning color {winning_color}")
            else:
                print (f"You have lost. The winning color {winning_color}")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)



screen.exitonclick()
