from tkinter import *
from tkinter.ttk import Combobox

root = Tk()
l = ["Java", "C++", "Python", "Mojo"]
combo = Combobox(root, values=l)

combo.pack()
root.mainloop()
