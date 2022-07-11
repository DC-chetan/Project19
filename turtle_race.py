from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500 , height = 400)
user_bet = screen.textinput(title="Make your Bet ", prompt="Which Turtle will win the race")
colors_sc=["red","blue", "orange","green", "purple","yellow"]
xv =-90
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors_sc[i])
    tim.penup()
    xv +=35
    tim.goto(x=-230, y=xv)


screen.exitonclick()