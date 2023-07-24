from tkinter import *
from tkinter import messagebox


def do_nothing():
    messagebox.askyesno("confirm", "click yes to proceed")


root = Tk()
frame = LabelFrame(root, text="frame1", padx=5, pady=5)
label = Label(frame, text="Enter your name: ")
label.pack()
entry = Entry(frame)
entry.pack()
button = Button(frame, text="ok", command=do_nothing)
button.pack()
frame.pack()
root.geometry("300x300")
root.mainloop()
