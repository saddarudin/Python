from tkinter import *


def do_nothing():
    if text.get(1.0, END) == '\n':
        print("Halla bhana jawan")
    else:
        print(text.get(1.0, END))


root = Tk()
text = Text(root)
text.pack()
button = Button(root, text="search", command=do_nothing)
button.pack()
root.mainloop()
