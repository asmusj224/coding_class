# candy monster game
from tkinter import *
import random

# make window
window = Tk()
game_title = 'super mega ultra due guy man'
window.title(game_title)

canvas = Canvas(window, width=400, height=400, bg='blue')
canvas.pack()

title = canvas.create_text(200, 200, text=game_title,
                           fill='green', font=('helvetica', 20))
directions = canvas.create_text(
    200, 300, text=' collect candy but aviod read ones.', fill='green', font=('helvetica', 20))

score = 0
score_display = Label(window, text='Score: ' + str(score))
score_display.pack()

# level
level = 1
level_display = Label(window, text='level: ' + str(level))
level_display.pack()

# character
image_file = "spongebob.gif"
player_image = PhotoImage(file=image_file)
mychar = canvas.create_image(200, 360, image=player_image)


candy_list = []
bad_candy_list = []
candy_speed = 2
candy_colors_list = ["blue", "green", "pink",
                     "red", "yellow", "purple", "white"]


def make_candy():
    xposition = random.randint(1, 400)
    candy_color = random.choice(candy_colors_list)
    candy = canvas.create_oval(
        xposition, 0, xposition + 30, 30, fill=candy_color)
    candy_list.append(candy)

    if candy_color == "red":
        bad_candy_list.append(candy)

    window.after(1000, make_candy)


# def move_candy():
make_candy()
window.mainloop()
