# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# list_of_colors = []
#
# for x in range (30):
#     color = colors[x].rgb
#     col_tuple = (color.r, color.g, color.b)
#     list_of_colors.append(col_tuple)
#
# print(list_of_colors)

color_list = [(233, 222, 228), (190, 172, 0), (208, 0, 103), (0, 148, 60), (253, 69, 0), (217, 229, 234), (167, 0, 0), (0, 128, 205), (89, 0, 95), (254, 223, 0), (42, 192, 234), (0, 0, 0), (248, 19, 152), (253, 7, 4), (235, 11, 143), (253, 4, 6), (15, 190, 234), (236, 153, 69), (250, 51, 17), (238, 215, 82), (16, 167, 127), (224, 126, 168), (234, 163, 190), (114, 193, 156), (160, 210, 177), (142, 209, 228), (239, 170, 157), (106, 120, 184)]

from turtle import Turtle, Screen
from random import choice
tim = Turtle()
screen = Screen()
screen.colormode(255)

tim.up()
tim.speed(0)
# tim.setpos(-30,-30)

start_point = [-230 , -260]

for y in range(10):
    start_point[1] += 50
    tim.goto(tuple(start_point))
    for x in range(10):
        tim.dot(20, choice(color_list))
        tim.forward(50)

## OR Angela's code:
# import turtle as turtle_module
# import random
#
# turtle_module.colormode(255)
# tim = turtle_module.Turtle()
# tim.speed("fastest")
# tim.penup()
# tim.hideturtle()
# color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
# tim.setheading(225)
# tim.forward(300)
# tim.setheading(0)
# number_of_dots = 100
#
# for dot_count in range(1, number_of_dots + 1):
#     tim.dot(20, random.choice(color_list))
#     tim.forward(50)
#
#     if dot_count % 10 == 0:
#         tim.setheading(90)
#         tim.forward(50)
#         tim.setheading(180)
#         tim.forward(500)
#         tim.setheading(0)
#
# screen = turtle_module.Screen()
# screen.exitonclick()



screen.exitonclick()