import turtle
import random

turtle.colormode(255)
tim = turtle.Turtle()


color_list = [(239, 245, 250), (250, 242, 247), (243, 251, 246), (139, 164, 184), (27, 114, 171), (202, 141, 167), (237, 213, 67), (219, 157, 89), (22, 136, 66), (139, 21, 37), (124, 72, 94), (185, 176, 26), (70, 30, 37), (182, 73, 41), (225, 170, 197), (52, 36, 34), (232, 83, 40), (39, 174, 99), (108, 190, 136), (9, 107, 64), (29, 169, 185), (181, 95, 112), (38, 37, 43), (239, 216, 8), (188, 184, 210), (158, 207, 215), (152, 214, 174), (240, 169, 154), (105, 41, 39), (116, 120, 162), (71, 53, 93), (15, 100, 104), (4, 81, 21)]


def work():
    for i in range(10):
        tim.dot("20", random.choice(color_list))
        tim.penup()
        tim.forward(50)


tim.penup()
tim.hideturtle()
tim.setpos(-200, -250)
k = -200
tim.speed(0)
for i in range(10):
    tim.penup()
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    work()
    tim.setpos(-200, k)
    k += 50


screen = turtle.Screen()
screen.exitonclick()