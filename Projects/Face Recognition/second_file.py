import tkinter as tk
from tkinter import messagebox


def admin_selected():
    root.withdraw()
    options_window = tk.Toplevel(root)
    options_window.title("Admin Options")
    options_window.config(bg="#adaaa0")
    options_window.geometry("500x400+100+50")

    mark_attendance = tk.Button(options_window,
                                text="Mark Attendance",
                                cursor="hand2",
                                bg="#c91916",
                                fg="black",
                                font=("Arial", 14, "bold"),
                                width=15,
                                height=1,
                                command="")
    mark_attendance.place(x=170, y=80, width=170, height=30)

    add_student = tk.Button(options_window,
                            text="Add New Student",
                            cursor="hand2",
                            bg="#4b10c9",
                            fg="black",
                            font=("Arial", 14, "bold"),
                            width=15,
                            height=1,
                            command="")
    add_student.place(x=170, y=130, width=170, height=30)

    options_window.protocol("WM_DELETE_WINDOW", on_options_window_close)
    

def student_selected():
    messagebox.showinfo("Welcome My Obedient Student!")


def on_options_window_close():
    root.destroy()


root = tk.Tk()
root.title("Facial Recognition System")

label1 = tk.Label(root,
                  text="Select User Type:",
                  bg="#6dc910",
                  font=("Arial", 16, "bold"))
label1.pack(pady=20)

button1 = tk.Button(root,
                    text="Admin",
                    cursor="hand2",
                    bg="#c91916",
                    fg="black",
                    font=("Arial", 14, "bold"),
                    width=15,
                    height=1,
                    command=admin_selected)
button1.place(x=170, y=80, width=150, height=30)

button2 = tk.Button(root,
                    text="Student",
                    cursor="hand2",
                    bg="#4b10c9",
                    fg="black",
                    font=("Arial", 14, "bold"),
                    width=15,
                    height=1,
                    command=student_selected)
button2.place(x=170, y=130, width=150, height=30)

root.geometry("500x400+100+50")
root.config(bg="#adaaa0")
root.mainloop()
