from turtle import Turtle, Screen

tim = Turtle()

screen= Screen()
def left():
    newheading = tim.heading() + 10
    tim.setheading(newheading)
def right():
    newheading = tim.heading() - 10
    tim.setheading(newheading)
def forward_move():
    tim.forward(20)

def backward_mv():

    tim.forward(-20)

def clear_sc():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()

screen.onkey(left,"a")
screen.onkey(right,"d")
screen.onkey(forward_move,"w")
screen.onkey(backward_mv,"s")
screen.onkey(clear_sc, "x")


screen.exitonclick()
