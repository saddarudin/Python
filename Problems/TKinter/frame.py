from tkinter import *

root = Tk()

frame = Frame(root)
b1 = Button(frame, text="Button1")
b2 = Button(frame, text="Button2")
b3 = Button(frame, text="Button3")
b4 = Button(frame, text="Button4")
b1.pack()
b2.pack()
b3.pack()
b4.pack()

frame.pack()


root.mainloop()