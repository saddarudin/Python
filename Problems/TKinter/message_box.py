from tkinter import *
from tkinter import messagebox


def message():
    answer = messagebox.askyesno("Confirm message", "Do you want to continue?")
    if answer:
        root.quit()
    else:
        print("You said no!")


root = Tk()

b = Button(root, text="Proceed", command=message)
b.pack()
root.mainloop()
