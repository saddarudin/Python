from tkinter import *


def left_click(event):
    print("Left key is pressed")


def right_click(event):
    print("Right key is pressed")


def middle_click(event):
    print("Middle key is pressed")


root = Tk()

frame = Frame(root, width=200, height=200)

frame.bind("<Button-1>", left_click)
frame.bind("<Button-2>", middle_click)
frame.bind("<Button-3>", right_click)
frame.pack()

root.mainloop()
