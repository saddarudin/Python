from tkinter import *

root = Tk()

# l1 = Label(root, text="Halla Bhana Jawan!!!!", bg="black", fg="red")
b1 = Button(root, text="Button1", bg="Black", fg="blue")
# b2 = Button(frame, text="Button2")
# b3 = Button(frame, text="Button3")

b1.pack(side=BOTTOM, fill=Y)
# b2.pack(fill=Y, bg="Black", fg="blue", side=RIGHT)
# b3.pack(fill="both", bg="Red", fg="blue", side=RIGHT)
# l1.pack(fill=X)


root.mainloop()