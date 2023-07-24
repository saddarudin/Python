from tkinter import *

root = Tk()
canvas = Canvas(width=1000, height=1000, bg="white")
canvas.pack()
photo = PhotoImage(file="magic box.png")
canvas.create_image(0, 0, image=photo, anchor=NW)

root.mainloop()
