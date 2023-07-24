from tkinter import *


def fun(event):
    print("You are logged in. Welcome!")


root = Tk()

l1 = Label(root, text="Name: ")
l2 = Label(root, text="Password: ")
e1 = Entry(root)
e2 = Entry(root)
l1.grid(row=0, column=0, sticky=W)
l2.grid(row=1, column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
c = Checkbutton(root, text="Remember my credentials")
c.grid(row=2, columnspan=2)
b = Button(root, text="LogIn")
b.grid(row=3, column=0)
b.bind("<Button-1>", fun)

root.mainloop()
