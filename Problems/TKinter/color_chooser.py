from tkinter import *
from tkinter import colorchooser


def select_color():
    clr = colorchooser.askcolor(title="select color")
    root.configure(background=clr[1])


root = Tk()
button = Button(root, text="change color", command=select_color)
button.pack()

root.geometry("300x300")
root.mainloop()
