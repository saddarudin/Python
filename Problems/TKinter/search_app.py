from tkinter import *
import wikipedia
from tkinter import messagebox


def search():
    text.delete(1.0, END)
    try:
        answer = wikipedia.summary(entry.get())
        text.insert(INSERT, answer)
    except:
        text.insert(INSERT, "check your internet connection or input string")


root = Tk()
frame1 = Frame(root)
entry = Entry(frame1, width=30)
button = Button(frame1, text="search", command=search, width=10)
entry.pack()
button.pack()
frame1.pack(side=TOP)

frame2 = Frame(root)
text = Text(frame2, width=40, height=15, wrap=WORD, padx=5, pady=5)
scroll = Scrollbar(frame2, command=text.yview)
text.config(yscrollcommand=scroll.set)
scroll.pack(side=RIGHT, fill=Y)
text.pack(side=LEFT)
frame2.pack()

root.geometry("400x300+50+50")
root.mainloop()
