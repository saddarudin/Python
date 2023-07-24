from tkinter import *
from tkinter import messagebox


def click_me():
    if i.get() == 0:
        messagebox.showinfo("Result", "Male")
    else:
        messagebox.showinfo("Result", "Female")


root = Tk()

i = IntVar()
radio1 = Radiobutton(root, text="male", value=0, variable=i)
radio2 = Radiobutton(root, text="female", value=1, variable=i)
b = Button(root, text='Ok', command=click_me)
radio1.pack()
radio2.pack()
b.pack()
root.mainloop()
