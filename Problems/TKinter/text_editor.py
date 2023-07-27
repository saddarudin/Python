from tkinter import *
from tkinter import filedialog


class WriteNote:

    def open_file(self):
        x = filedialog.askopenfile(initialdir="/", title="open file", filetypes=(("text files", "*.txt"),("all files", "*.*")))
        if x is not None:
            self.text_area.delete(1.0, END)
            for line in x:
                self.text_area.insert(END, line)
        x.close()

    def save_as_file(self):
        f = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
        if f is None:
            return
        f.write(self.text_area.get(1.0, END))
        f.close()

    def __init__(self, master):
        self.master = master
        master.title("Text Editor")
        self.text_area = Text()
        self.text_area.pack(fill=BOTH, expand=1)
        self.main_menu = Menu()
        self.master.config(menu=self.main_menu)
        self.file = Menu()
        self.main_menu.add_cascade(label="File", menu=self.file)
        self.edit = Menu()
        self.main_menu.add_cascade(label="edit", menu=self.edit)
        self.view = Menu()
        self.main_menu.add_cascade(label="view", menu=self.view)
        self.file.add_command(label="open", command=self.open_file)
        self.file.add_command(label="save", command="")
        self.file.add_command(label="save as", command="")
        self.edit.add_command(label="rename", command="")
        self.edit.add_command(label="delete", command="")
        self.edit.add_command(label="change extension", command="")
        self.view.add_command(label="horizontal", command="")
        self.view.add_command(label="vertical", command="")
        self.view.add_command(label="full screen", command="")
        self.view.add_command(label="half screen", command="")



root = Tk()
notepad = WriteNote(root)
root.geometry("300x300+50+50")
root.mainloop()

