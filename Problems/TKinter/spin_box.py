from tkinter import *


def print_me():
    print(spin.get())


root = Tk()
spin = Spinbox(root, from_=1, to=10)
spin.pack()
button = Button(root, text="print", command=print_me)
button.pack()
root.geometry("300x300+50+50")
root.mainloop()
