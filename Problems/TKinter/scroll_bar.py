from tkinter import *

root = Tk()
frame = Frame(root)
bar = Scrollbar(frame)
l = Listbox(frame)
for i in range(1, 51):
    l.insert(END, f"list {i}")

l.config(yscrollcommand=bar.set)
bar.config(command=l.yview)

bar.pack(side=RIGHT, fill=Y)
l.pack(side=LEFT)
frame.pack()
root.mainloop()
