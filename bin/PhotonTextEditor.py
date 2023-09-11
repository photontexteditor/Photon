import tkinter #importing tkinter 
import customtkinter as ctk #import customtkinter and renaming it "ctK"

# appearance
ctk.set_appearance_mode("System") 
ctk.set_default_color_theme("dark-blue")

# class/blueprint
class Photon(ctk.CTk):
    def __init__(self):
        super().__init__() # using super method to inherit all the attributes of base class to derived class

        # geometry of Photon Text Editor
        self.title("Photon Text Editor")
        self.geometry(f"{1920}x{1080}")

        # sidebar

        # textbox
        self.textbox = ctk.CTkTextbox(self, width=1920, height=1080)
        self.textbox.grid(row=0, column=1, padx=(0,0), pady=(0, 0), sticky="nsew")

if __name__ == "__main__":
    obj = Photon()
    obj.mainloop()