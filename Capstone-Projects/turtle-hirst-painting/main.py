import colorgram
from turtle import Turtle
from random import choice

image_file = r'./hirst-dots-image.jpg'

def extract_RGB_color_list(image_file, number = 1):
    """Returns the list of RGB color tuples extracted from a input image file. 
    The number of color extracted can also be another input with default value 1."""

    colors_list = []
    colors = colorgram.extract(image_file, number)

    for color in colors:
        rgb_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
        colors_list.append(rgb_tuple)

    return colors_list

# print(extract_RGB_color_list(image_file, 30))

def get_random_color():
    
    # List of RGB Colors.    
    color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), 
    (196, 145, 171), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120), 
    (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), 
    (48, 156, 194), (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), 
    (112, 123, 149), (229, 174, 165), (172, 203, 182), (158, 205, 215), (69, 58, 47), 
    (108, 47, 60), (53, 70, 65), (72, 64, 53)]

    return choice(color_list)

neel = Turtle()

def draw_hirst_dot_images(n_rows, n_cols):
    """Draws Hirst's dot images with turtle graphics."""

    # Set the initial parameters.
    neel.screen.colormode(255)
    neel.speed("fast")
    neel.hideturtle()

    for row in range(n_rows):
        neel.penup()
        neel.setx(-250)
        neel.sety(-200 + row * 50)

        for col in range(n_cols): 
            neel.dot(20, get_random_color())
            neel.forward(50)
    
    

draw_hirst_dot_images(10, 10)


neel.screen.mainloop()

