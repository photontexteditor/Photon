import tkinter #importing tkinter 
import tkinter.messagebox #import tkinter.messagebox for pop-up warning, info, etc.
import customtkinter as ctk #import customtkinter and renaming it "ctk"

# appearance mode
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# class/blueprint
class PhotonTextEditor(ctk.CTk):
    def __init__(self):
        super().__init__() # using super method to inherit all the attributes of base class to derived class

        # geometry of editor
        self.title("Photon Text Editor")
        self.geometry(f"{1920}x{1080}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=100, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # logo
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Photon Text Editor", font=ctk.CTkFont(size=15, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="File")
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Edit")
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="More")
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        # appearance mode
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        
        # scaling label
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create tabview
        self.tabview = ctk.CTkTabview(self, width=100)
        self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        self.tabview.add("Font")
        self.tabview.add("Align")
        self.tabview.add("Color")
        self.tabview.tab("Font").grid_columnconfigure(0, weight=1)  
        
        # configure grid of individual tabs
        self.tabview.tab("Align").grid_columnconfigure(0, weight=1)

        # option menu
        self.optionmenu_1 = ctk.CTkOptionMenu(self.tabview.tab("Font"), dynamic_resizing=False, values=["Family", "Times New Roman", "Arial", "Monteserrat"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # combobox
        self.combobox_1 = ctk.CTkComboBox(self.tabview.tab("Font"),values=["Size", "2", "4", "6", "8", "10", "11", "12", "14", "16"])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
       
       #input button
        self.string_input_button = ctk.CTkButton(self.tabview.tab("Font"), text="Color",command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = ctk.CTkLabel(self.tabview.tab("Align"), text="Left, Middle, Right")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create textbox
        self.textbox = ctk.CTkTextbox(self, width=250, height=1000)
        self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

        #set default values
        self.sidebar_button_3.configure(state="disabled", text="Save")
        self.appearance_mode_optionemenu.set("Dark")

    # functionalities
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

# The statement if __name__ == "__main__": is used to check whether the current Python module is being run as the main program or if it is being imported as a module into another program. When a Python module is imported, it is given a name based on the file name.
if __name__ == "__main__":
    app = PhotonTextEditor()
    app.mainloop()