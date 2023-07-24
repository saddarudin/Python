from tkinter import *
from tkinter import messagebox


def fun(event):
    messagebox.showinfo("Message", "You've successfully logged in")


root = Tk()
frame = Frame(root, width=300, height=300)
label1 = Label(frame, text="Enter your name: ")
label2 = Label(frame, text="Enter your password: ")
label1.place(x=10, y=10)
label2.place(x=10, y=30)
entry1 = Entry(frame)
entry2 = Entry(frame)
entry1.place(x=150, y=10)
entry2.place(x=150, y=30)
button = Button(frame, text="Proceed")
button.bind("<Button-1>", fun)
button.place(x=200, y=230)

frame.pack()
root.mainloop()
