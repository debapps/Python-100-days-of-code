from turtle import Turtle, Screen
from random import randint

# Screen set up
screen = Screen()
screen.setup(width=500, height=400)
screen.title("Turtle Race")
screen.bgcolor("gray")
user_bet = screen.textinput(title="Enter your bet", prompt="Which turtle will win the race? Enter a color: ")


# List of rainbow colors.
colors = ["purple", "blue", "green", "yellow", "orange", "red"]

# Generate turtle of input color and position.
def generate_turtle(color, y_pos):
    neel = Turtle(shape="turtle")
    neel.color(color)
    neel.penup()
    neel.goto(x=-230, y=y_pos)
    return neel

# Move the input turtle forward random distance. 
def move_turtle(turtle):
    random_distance = randint(0, 10)
    turtle.forward(random_distance)

# List of turtle.
turtle_list = []

for n in range(6):
    y_pos = -120 + n * 40
    my_turtle = generate_turtle(colors[n], y_pos)
    turtle_list.append(my_turtle)

is_race_on = False

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        move_turtle(turtle)

        if turtle.xcor() >= 230:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You've won! {winning_turtle.title()} wins the race.")
            else:
                print(f"You've lost! {winning_turtle.title()} wins the race.")
            break
                
        

screen.exitonclick()

