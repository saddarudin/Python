import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
from tkinter import PhotoImage


def admin_selected():
    password = simpledialog.askstring("Password", "Enter Password:", show='*')
    if password == '12345':
        root.withdraw()
        options_window = tk.Toplevel(root)
        options_window.title("Admin Options")
        frame = tk.Frame(options_window)
        options_window.config(bg="#adaaa0")
        options_window.geometry("500x400+100+50")
        mark_attendance = tk.Button(frame,
                                        text="Mark Attendance",
                                        cursor="hand2",
                                        bg="#c91916",
                                        fg="black",
                                        font=("Arial", 14, "bold"),
                                        width=15,
                                        height=1,
                                        command="")
        mark_attendance.place(x=170, y=80, width=170, height=30)
        add_student = tk.Button(frame,
                                text="Add New Student",
                                cursor="hand2",
                                bg="#4b10c9",
                                fg="black",
                                font=("Arial", 14, "bold"),
                                width=15,
                                height=1,
                                command="")
        add_student.place(x=170, y=130, width=170, height=30)
        mark_attendance.grid(row=0, column=0)
        add_student.grid(row=1, column=0)
        def adjust_frame(event):
            w = options_window.winfo_width()
            h = options_window.winfo_height()
            frame_w = frame.winfo_width()
            frame_h = frame.winfo_height()
            frame.place(x= (w - frame_w)//2, y= (h - frame_h)//2)
            
        options_window.bind("<Configure>", adjust_frame)
        adjust_frame(None)
        options_window.protocol("WM_DELETE_WINDOW", on_options_window_close)
    else:
        messagebox.showerror("Error Message!", "incorrect password!")


def student_selected():
    messagebox.showinfo("Welcome My Obedient Student!")


def on_options_window_close():
    root.destroy()


root = tk.Tk()
root.title("Facial Recognition System")
frame = tk.Frame(root)
label1 = tk.Label(frame,
                  text="Select User Type:",
                  bg="#6dc910",
                  width=15, 
                  height=1,
                  font=("Arial", 16, "bold"))
label1.place(x=160, y=0, width=170, height=30)

button1 = tk.Button(frame,
                    text="Admin",
                    cursor="hand2",
                    bg="#c91916",
                    fg="black",
                    font=("Arial", 14, "bold"),
                    width=16,
                    height=1,
                    command=admin_selected)
button1.place(x=170, y=80)

button2 = tk.Button(frame,
                    text="Student",
                    cursor="hand2",
                    bg="#4b10c9",
                    fg="black",
                    font=("Arial", 14, "bold"),
                    width=16,
                    height=1,
                    command=student_selected)
button2.place(x=170, y=130)


label1.grid(row=0, column=0)
button1.grid(row=1, column=0)
button2.grid(row=2, column=0)

def adjust_frame(event):
    w = root.winfo_width()
    h = root.winfo_height()
    frame_w = frame.winfo_width()
    frame_h = frame.winfo_height()
    frame.place(x= (w - frame_w)//2, y= (h - frame_h)//2)


root.bind("<Configure>", adjust_frame)
adjust_frame(None)
root.geometry("500x400+100+50")
root.config(bg="#adaaa0")
root.mainloop()
