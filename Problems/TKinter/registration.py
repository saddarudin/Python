from tkinter import *
from tkinter import messagebox


def click_me():
    if entry.get() == "saddar":
        messagebox.showinfo("successful")
    else:
        messagebox.showinfo("try again!")


root = Tk()
entry = Entry(root)
entry.place(x=10, y=10)
button = Button(root, text="login", command=click_me)
button.place(x=30, y=40)

root.mainloop()
