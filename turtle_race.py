from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500 , height = 400)
user_bet = screen.textinput(title="Make your Bet ", prompt="Which Turtle will win the race")
colors_sc=["red","blue", "orange","green", "purple","yellow"]
xv =-90
all_turtles = []
for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors_sc[i])
    new_turtle.penup()
    xv +=35
    new_turtle.goto(x=-230, y=xv)
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on = False
            winning_colour = turtle.pencolor()
            if winning_colour==user_bet:
                print(f"You've won the race and the winning color is {winning_colour}")
            else:
                print(f"You've lost the race and the winning color is {winning_colour}")
        rand_distance=random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()