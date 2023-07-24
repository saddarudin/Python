from tkinter import *


def print_me():
    # print(text.get(1.0, END))
    print(text.selection_get())


def clear():
    text.delete(1.0, END)


root = Tk()
text = Text(root, width=40, height=10, wrap=WORD, padx=5, pady=5)
text.pack()

button = Button(root, text="print me", command=print_me)
button.pack()
b = Button(root, text="clear", command=clear)
b.pack()

root.geometry("400x400+50+50")
root.mainloop()
