from tkinter import *


def do_nothing():
    print("I'm doing nothing")


root = Tk()
main_menu = Menu(root)
root.config(menu=main_menu)
file = Menu(main_menu)
main_menu.add_cascade(label="file", menu=file)

edit = Menu(main_menu)
main_menu.add_cascade(label="edit", menu=edit)

file.add_command(label="new file", command=do_nothing)
file.add_separator()
save = Menu(file)
save.add_command(label="desktop", command=do_nothing)
save.add_command(label="c drive", command=do_nothing)
file.add_cascade(label="save", menu=save)
file.add_command(label="save as", command=do_nothing)
edit.add_command(label="rename", command=do_nothing)
edit.add_command(label="cut", command=do_nothing)


root.mainloop()
