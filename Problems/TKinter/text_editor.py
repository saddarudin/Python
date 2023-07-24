from tkinter import *


class ClickHere:
    def __init__(self, master):
        self.master = master
        self.master.title("text editor")
        self.text = Text()
        self.text.pack(fill=BOTH, expand=1)
        self.main_menu = Menu(self.master)
        self.file_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)
        self.edit_menu = Menu(self.main_menu)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)


root = Tk()
te = ClickHere(root)
root.mainloop()
