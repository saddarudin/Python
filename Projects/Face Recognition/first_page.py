import tkinter as tk
from tkinter import messagebox


def show_options():
    selected_user = user_var.get()

    if selected_user == "admin":
        root.withdraw()
        options_window = tk.Toplevel(root)
        options_window.title("Admin Options")

        mark_attendance_label = tk.Label(options_window, text="Mark Attendance")
        mark_attendance_label.pack()

        add_student_label = tk.Label(options_window, text="Add New Student")
        add_student_label.pack()

        options_window.protocol("WM_DELETE_WINDOW", on_options_window_close)
    else:
        messagebox.showinfo("Student", "You are logged in as a Student.")


def on_options_window_close():
    root.deiconify()
    root.focus_set()


root = tk.Tk()
root.title("Facial Recognition Web App")

user_var = tk.StringVar()

user_label = tk.Label(root, text="Select User Type:")
user_label.pack()

admin_label = tk.Label(root, text="Admin", cursor="hand2")
admin_label.pack()
admin_label.bind("<Button-1>", lambda event: show_options())

student_label = tk.Label(root, text="Student", cursor="hand2")
student_label.pack()
student_label.bind("<Button-1>", lambda event: messagebox.showinfo("Student", "You are logged in as a Student."))


root.geometry("300x300+100+50")
root.mainloop()
