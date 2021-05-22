from tkinter import *

window = Tk()

window.title("Hello World")
window.geometry('400x150')

# Event handler function. Called when the button is clicked


def hello_world():
    print("Hello world event handler")  # prints to the shell
    display_area.config(text="Hello, World", fg="yellow",
                        bg="black")  # changes display of label


button1 = Button(window, text="Click Me", bg='blue',
                 fg='white', command=hello_world)
button1.pack()  # places button on the screen

display_area = Label(window, text="")
display_area.pack()  # places label on the screen

# Create a new button to clear out the text when clicked.

window.mainloop()
