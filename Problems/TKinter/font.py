from tkinter import *
from tkinter.font import Font

root = Tk()
font = Font(family="Poppins", size=16, weight="bold", slant="italic", underline=1)

label = Label(root, text="The Dream Team!", font=font)
label.place(x=40, y=100)

root.geometry("300x300+50+50")
root.mainloop()
