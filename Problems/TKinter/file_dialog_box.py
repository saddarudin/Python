from tkinter import *
from tkinter import filedialog


def open_file():
    result = filedialog.askopenfile(initialdir="/", title="select file", filetypes=(("text files", ".txt"), ("all files", "*.*")))
    for i in result:
        print(i)


root = Tk()
button = Button(root, text="open file", command=open_file)
button.pack()
root.geometry("300x300")
root.mainloop()
