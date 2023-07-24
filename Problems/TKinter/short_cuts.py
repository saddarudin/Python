from tkinter import *
from tkinter import messagebox


def call_me(event=""):
    result = messagebox.showinfo("confirmation message", "press OK")
    if result == "ok":
        root.destroy()


root = Tk()
root.bind("<Control-c>", call_me)
button = Button(root, text="close", command=call_me)
button.pack()
root.geometry("300x300")
root.mainloop()
