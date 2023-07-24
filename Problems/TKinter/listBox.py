from tkinter import *


def selected_items():
    items = l.curselection()
    for i in items:
        print(l.get(i))


root = Tk()
l = Listbox(root, selectmode=MULTIPLE)
l.insert(1, "C")
l.insert(2, "C++")
l.insert(3, "Java")
l.insert(4, "Python")
l.insert(5, "R")
l.insert(6, "Ruby")
l.insert(7, "Perl")
l.insert(8, "Java Script")
l.insert(9, "Type Script")
l.insert(10, "C sharp")
l.insert(11, "Dart")
l.insert(12, "Mojo")
l.pack()
button = Button(root, text="OK", command=selected_items)
button.pack()

root.geometry("500x500+200+100")
root.mainloop()
