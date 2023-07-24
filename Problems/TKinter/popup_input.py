from tkinter import *
from tkinter import simpledialog


def popup():
    s = simpledialog.askstring("input string", "enter your name: ")
    print(s)


root = Tk()
button = Button(root, text='next', command=popup)
button.pack()
root.mainloop()
