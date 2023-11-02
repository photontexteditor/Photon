import tkinter as tk #importing tkinter 
import customtkinter as ctk #import customtkinter and renaming it "ctK"
from tkinter import ttk 
from tkinter import font, colorchooser, filedialog, messagebox
import os 

# appearance mode
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# class/blueprint
class Photon(ctk.CTk):
    def __init__(self):
        super().__init__() # using super method to inherit all the attributes of base class to derived class

        # geometry of editor
        self.title("Photon Text Editor")
        self.geometry(f"{1920}x{1080}")
        self.wm_iconbitmap('photon.ico')

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew") # rowspan=4
        # self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # logo
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Photon Text Editor", font=ctk.CTkFont(size=15, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
    
        # font
        self.font_tuple = tk.font.families()
        self.font_family = ctk.StringVar()
        self.combobox_1 = ctk.CTkComboBox(self.sidebar_frame, values=self.font_tuple, variable=self.font_family, state="readonly")
        self.combobox_1.set('Arial')
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        
        # size box 
        self.size_var = ctk.StringVar()
        self.font_size = ['2', '4', '6', '8', '9', '10']
        self.combobox_2 = ctk.CTkComboBox(self.sidebar_frame, values=self.font_size, variable=self.size_var, state="readonly")
        self.combobox_2.set('2')
        self.combobox_2.grid(row=2, column=0, padx=20, pady=(10, 10))

        # button
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Edit")
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="More")
        self.sidebar_button_3.grid(row=5, column=0, padx=20, pady=10)

        # appearance mode
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=7, column=0, padx=20, pady=(10, 10))
        
        # scaling label
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=8, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=9, column=0, padx=20, pady=(10, 20))

        # create textbox
        self.textbox = ctk.CTkTextbox(self, width=250, height=770)
        self.textbox.grid(row=0, column=1, padx=(10, 10), pady=(20, 10), sticky="nsew")

        self.sidebar_button_3.configure(state="disabled", text="Save")
        self.appearance_mode_optionemenu.set("Dark")

    def open_input_dialog_event(self):
        dialog = ctk.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")


if __name__ == "__main__":
    app = Photon()
    app.mainloop()
