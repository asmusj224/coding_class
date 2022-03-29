import turtle
import random

yellow = "yellow"
black = 'black'
eye_color = input("What is your eye color? ")
pen = turtle.Pen()
pen.speed(0)
pen.hideturtle()
turtle.bgcolor(black)


def draw_smile(x, y):
    print(x, y)
    pen.penup()
    pen.setpos(x, y)
    pen.pendown()
    draw_face()
    # left eye
    draw_eye(x - 15, y + 60)
    # right eye
    draw_eye(x + 15, y + 60)
    draw_mouth(x, y)


def draw_face():
    pen.pencolor(yellow)
    pen.fillcolor(yellow)
    pen.begin_fill()
    pen.circle(50)
    pen.end_fill()


def draw_eye(x, y):
    pen.setpos(x, y)
    pen.fillcolor(eye_color)
    pen.begin_fill()
    pen.circle(10)
    pen.end_fill()


def draw_mouth(x, y):
    pen.setpos(x - 25, y + 40)
    pen.pencolor(black)
    pen.width(10)
    pen.goto(x - 10, y + 20)
    pen.goto(x + 10, y + 20)
    pen.goto(x + 25, y + 40)
    pen.width(1)



#turtle.onscreenclick(draw_smile)
draw_smile(0, 0)
draw_smile(200, -100)
turtle.mainloop()
