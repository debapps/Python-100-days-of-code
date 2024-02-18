from turtle import Turtle
from random import choice, randrange

jimmy = Turtle()
jimmy.screen.bgcolor("black")
jimmy.screen.colormode(255)

# Challenge: 1 - Draw a square.
# for _ in range(4):
#     jimmy.forward(100)
#     jimmy.left(90)

# Challenge: 2 - Draw a dashed line
# for _ in range(50):
#     jimmy.forward(5)
#     jimmy.penup()
#     jimmy.forward(2)
#     jimmy.pendown()

# Challenge: 3 - Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon.

# def draw_turtle_shape(jim, side, color, length):
#     jim.color(color)
#     angle = 360 / side
#     for _ in range(side):
#         jim.forward(length)
#         jim.right(angle)

# color_list = ["blue violet", "chartreuse", "cyan", "yellow",
#               "purple", "red", "dodger blue", "spring green"]
# color_idx = 0

# for side in range(3, 11):    
#     draw_turtle_shape(jimmy, side, color_list[color_idx], 100)
#     color_idx += 1

# Challenge: 4 - Draw a random walk.

# Get random angles between 90, 180, 270.
# def get_random_angle():
#     return (90 * randrange(0, 4))

# Get a random color.
def get_random_color():
    # colors = ["cornflower blue", "medium blue", "dark blue", "midnight blue",
    #           "deep sky blue", "gray", "teal", "turquoise", "light sea green",
    #           "pale green", "olive drab", "lawn green", "yellow", "olive", 
    #           "dark orange", "navajo white", "saddle brown", "bisque", "firebrick",
    #           "tomato", "crimson", "maroon", "rosy brown", "light pink", "hot pink",
    #           "purple", "magenta", "blue violet", "indigo", "slate blue", "ghost white"]
    # return choice(colors)

    return tuple((randrange(0, 256), randrange(0, 256), randrange(0, 256)))

# jimmy.shape("circle")
# jimmy.turtlesize(0.5, 0.5, 0)
# jimmy.speed("fast")
# jimmy.width(10)

# for _ in range(200):
#     jimmy.color(get_random_color())
#     jimmy.left(get_random_angle())
#     jimmy.forward(30)


# Challenge: 5 - Draw a spirograph.
jimmy.speed("fastest")

def draw_spirograph(gap):
    for step in range(int(360 / gap)):
        jimmy.color(get_random_color())
        jimmy.circle(100.0)
        jimmy.setheading(jimmy.heading() + gap)

draw_spirograph(7)

    

jimmy.screen.mainloop()