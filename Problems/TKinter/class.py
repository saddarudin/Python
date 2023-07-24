from tkinter import *


class ButtonClass:

    def __init__(self, master):
        self.b1 = Button(master, text="Save", command=self.save)
        self.b1.pack()
        self.b2 = Button(master, text="Quit", command=master.quit)
        self.b2.pack()

    def save(self):
        print("You saved your progress")


root = Tk()
b = ButtonClass(root)
root.mainloop()
