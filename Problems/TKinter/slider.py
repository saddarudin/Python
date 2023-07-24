from tkinter import *
from tkinter import messagebox


def show_slider_position():
    messagebox.showinfo("slider position", "Current position is: "+str(s.get()))


root = Tk()

s = Scale(root, orient=HORIZONTAL, from_=0, to=100)
s.set(50)
s.pack()
b = Button(root, text="show position", command=show_slider_position)
b.pack()

root.mainloop()

