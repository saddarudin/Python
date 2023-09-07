import tkinter
import tkinter.messagebox
import customtkinter
from tkinter import simpledialog

customtkinter.set_appearance_mode("Dark")  
customtkinter.set_default_color_theme("blue") 


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.user = ''


        # configure window
        self.title("Face Recognition Attandence System")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="Main Menu", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, text="Mark Attandance", command=self.button_1_selected)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, text="Add New Student", command=self.button_2_selected)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame,text="Check Attendance", command=self.button_3_selected)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # set default values
        self.appearance_mode_optionemenu.set("Dark")
        self.scaling_optionemenu.set("100%")


    # def open_input_dialog_event(self):
    #     dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
    #     print("CTkInputDialog:", dialog.get_input())





    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def button_1_selected(self):
        print('Button 1 selected')

    def button_2_selected(self):
        print('Button 2 selected')

    def button_3_selected(self):
        print('Button 3 selected')


    # def sidebar_button_event(self):
    #     print("sidebar_button click")
        


    def setting_user_frame(self):
        if self.user == 'student':
            self.sidebar_button_1.configure(state="disabled")
            self.sidebar_button_2.configure(state='disabled')
        
            







class UserTypeSelection(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        # Configure window
        self.title("User Type Selection")
        self.geometry(f"{400}x{200}")

        # Configure grid layout (2x1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        # Create label for message
        message_label = customtkinter.CTkLabel(self, text="Are you a Student or Teacher?", font=customtkinter.CTkFont(size=16, weight="bold"))
        message_label.grid(row=0, column=0, padx=20, pady=20)

        # Create frame for buttons
        button_frame = customtkinter.CTkFrame(self)
        button_frame.grid(row=1, column=0, padx=20, pady=20)

        # Create "Student" button
        student_button = customtkinter.CTkButton(button_frame, text="Student", command=self.select_student)
        student_button.grid(row=0, column=0, padx=10)

        # Create "Teacher" button
        teacher_button = customtkinter.CTkButton(button_frame, text="Teacher", command=self.select_teacher)
        teacher_button.grid(row=0, column=1, padx=10)

    def select_student(self):
        ap = App()
        ap.user = 'student'
        app.destroy() 
        ap.setting_user_frame()
        ap.mainloop()

    def select_teacher(self):
        ap = App()
        ap.user = 'teacher'
        app.destroy()
        ap.mainloop()

    


if __name__ == "__main__":
    # user_type_selection()
    app = UserTypeSelection()
    # # app = App()
    app.mainloop()