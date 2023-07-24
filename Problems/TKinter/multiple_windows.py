from tkinter import *


def new_window():
    top = Toplevel()
    top.geometry("300x300+50+50")
    button = Button(top, text="submit", command=top.destroy)
    button.pack()


root = Tk()
root.geometry("300x300+50+50")
button1 = Button(root, text="next", command=new_window)
button1.pack()
root.mainloop()
