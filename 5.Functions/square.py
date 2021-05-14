import turtle

shelly = turtle.Turtle()


def square():
    for i in range(4):
        shelly.forward(100)
        shelly.left(90)


square()
shelly.forward(100)
square()
shelly.forward(100)
square()
