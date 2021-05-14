import turtle  # This line brings in the turtle module which will allow us to draw shapes

shelly = turtle.Turtle()

shelly.shape('turtle')

for i in range(6):
    for j in range(4):
        shelly.forward(100)
        shelly.left(90)
    shelly.right(60)
