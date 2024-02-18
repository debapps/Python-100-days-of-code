from turtle import Turtle, Screen

neel = Turtle()
screen = Screen()


def move_forward():
    neel.forward(20)


screen.listen()
screen.onkey(key="space", fun=move_forward)
    
screen.exitonclick()