import tkinter as tk #importing tkinter 
import customtkinter as ctk #import customtkinter and renaming it "ctK"
from tkinter import ttk 
from tkinter import font, colorchooser, filedialog, messagebox
from PIL import Image
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
        self.iconbitmap('photon.ico')

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew") # rowspan=4
        # self.sidebar_frame.grid_rowconfigure(4, weight=1)

        # logo
        self.logo_label1 = ctk.CTkLabel(self.sidebar_frame, text="Photon Text Editor", font=ctk.CTkFont(size=15, weight="bold"))
        self.logo_label1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.logo_label2 = ctk.CTkLabel(self.sidebar_frame, text="Text Editor", font=ctk.CTkFont(size=15, weight="bold"))
        # self.logo_label2.grid(row=1, column=0, padx=20, pady=(20, 10))
    
        # font
        self.font_tuple = tk.font.families()
        self.font_family = ctk.StringVar()
        self.font_box = ctk.CTkComboBox(self.sidebar_frame, values=self.font_tuple, variable=self.font_family, state="readonly", width=215)
        self.font_box.set('Arial')
        self.font_box.grid(row=0, column=1, padx=20, pady=(10, 10))
        
        # size box 
        self.size_tuple = ['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24', '28', '30', '34', '38', '40', '44', '48']
        self.size_var = tk.IntVar()
        self.font_size = ctk.CTkComboBox(self.sidebar_frame, values=self.size_tuple, variable=self.size_var, state="readonly", width=85)
        self.font_size.set('4')
        self.font_size.grid(row=0, column=2, padx=20, pady=(10, 10))

        # # bold button 
        # self.bold_icon = ctk.CTkImage(light_image=Image.open('icons/bold.png'), size=(40,40))
        self.bold_btn = ctk.CTkButton(self.sidebar_frame, text="Bold", font=ctk.CTkFont(size=15, weight="bold"))
        self.bold_btn.grid(row=0, column=3, padx=2, pady=2)


        # # italic button 
        # self.italic_icon = ctk.CTkImage(light_image=Image.open('icons/italic.png'), size=(10,10))
        self.italic_btn = ctk.CTkButton(self.sidebar_frame, text="Italic", font=ctk.CTkFont(size=15, weight="bold"))
        self.italic_btn.grid(row=0, column=4, padx=2, pady=2)

        # # underline button 
        # self.underline_icon = ctk.CTkImage(light_image=Image.open('icons/underline.png'), size=(10,10))
        self.underline_btn = ctk.CTkButton(self.sidebar_frame, text="Underline", font=ctk.CTkFont(size=15, weight="bold"))
        self.underline_btn.grid(row = 0, column=5, padx=2, pady=2)

        # # font color button 
        # self.font_color_icon = ctk.CTkImage(light_image=Image.open('icons/font_color.png'), size=(10,10))
        # self.font_color_btn = ctk.CTkButton(self.sidebar_frame, image=self.font_color_icon)
        # self.font_color_btn.grid(row=1, column=2, padx=5)

        # # align left 
        # self.align_left_icon = ctk.CTkImage(light_image=Image.open('icons/align_left.png'), size=(10,10))
        self.align_left_btn = ctk.CTkButton(self.sidebar_frame, text="Left")
        self.align_left_btn.grid(row=1, column=3, padx=2, pady=2)

        # # align center 
        # self.align_center_icon = ctk.CTkImage(light_image=Image.open('icons/align_center.png'), size=(10,10))
        self.align_center_btn = ctk.CTkButton(self.sidebar_frame, text="Center")
        self.align_center_btn.grid(row=1, column=4, padx=2, pady=2)

        # # align right 
        # self.align_right_icon = ctk.CTkImage(light_image=Image.open('icons/align_right.png'), size=(10,10))
        self.align_right_btn = ctk.CTkButton(self.sidebar_frame, text="Right")
        self.align_right_btn.grid(row=1, column=5, padx=2, pady=2)

        # # End toolbar


        # create tabview
        # self.tabview = ctk.CTkTabview(self.sidebar_frame, width=50)
        # self.tabview.grid(row=1, column=0, padx=(20, 0), pady=(20, 10))
        # self.tabview.add("CTkTabview")
        # self.tabview.add("Tab 2")
        # self.tabview.add("Tab 3")
        # self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        # self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

        # self.optionmenu_1 = ctk.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False, values=["Value 1", "Value 2", "Value Long Long Long"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.combobox_1 = ctk.CTkComboBox(self.tabview.tab("CTkTabview"),
        #                                             values=["Value 1", "Value 2", "Value Long....."])
        # self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
       
        # self.string_input_button = ctk.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",command=self.open_input_dialog_event)
        # self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        # self.label_tab_2 = ctk.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=10)

        # button
        # self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="Edit")
        # self.sidebar_button_2.grid(row=0, column=3, padx=20, pady=10)
        # self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, command=self.sidebar_button_event, text="More")
        # self.sidebar_button_3.grid(row=0, column=4, padx=20, pady=10)

        # appearance mode``
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=0, column=10, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],command=self.change_appearance_mode_event, width=100)
        self.appearance_mode_optionemenu.grid(row=1, column=10, padx=20, pady=(10, 10))
        
        # scaling label
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=0, column=11, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],command=self.change_scaling_event, width=90)
        self.scaling_optionemenu.grid(row=1, column=11, padx=20, pady=(10, 10))



        # # create tabview
        # self.tabview = ctk.CTkTabview(self, width=100)
        # self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.tabview.add("Font")
        # self.tabview.add("Align")
        # self.tabview.add("Color")
        # self.tabview.tab("Font").grid_columnconfigure(0, weight=1)  
        
        # # configure grid of individual tabs
        # self.tabview.tab("Align").grid_columnconfigure(0, weight=1)

        # self.optionmenu_1 = ctk.CTkOptionMenu(self.tabview.tab("Font"), dynamic_resizing=False, values=["Family", "size", "color"])
        # self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        # self.combobox_1 = ctk.CTkComboBox(self.tabview.tab("Font"),values=["Size", "Value 2", "Value Long....."])
        # self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
       
        # self.string_input_button = ctk.CTkButton(self.tabview.tab("Font"), text="Color",command=self.open_input_dialog_event)
        # self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        # self.label_tab_2 = ctk.CTkLabel(self.tabview.tab("Align"), text="Left, Middle, Right")
        # self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

        # create textbox
        self.textbox = ctk.CTkTextbox(self, width=1420, height=650)
        self.textbox.grid(row=4, column=0, padx=(10, 10), pady=(10, 10), sticky="nsew")

        # color theme
        # theme_choice = ctk.StringVar()
        # color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

        # color_dict = {
        #     'Light Default ' : ('#000000', '#ffffff'),
        #     'Light Plus' : ('#474747', '#e0e0e0'),
        #     'Dark' : ('#c4c4c4', '#2d2d2d'),
        #     'Red' : ('#2d2d2d', '#ffe8e8'),
        #     'Monokai' : ('#d3b774', '#474747'),
        #     'Night Blue' :('#ededed', '#6b9dc2')
        # }

        # font family and font size functionality 
        current_font_family = self.font_family.get()
        current_font_size = self.size_var.get()

        def change_font(event=None):
            global current_font_family
            current_font_family = self.font_family.get()
            self.textbox.configure(font=(ctk.CTkFont(family=current_font_family)))

        def change_fontsize(event=None):
            global current_font_size
            current_font_size = self.size_var.get()
            self.textbox.configure(font=(ctk.CTkFont(size=current_font_size)))
        
        self.font_box.configure(command=change_font)
        self.font_size.configure(command=change_fontsize)
        

        # bold button functionality
        def change_bold():
            text_property = tk.font.Font(font=self.textbox['font'])
            if text_property.actual()['weight'] == 'normal':
                self.textbox.configure(font=ctk.CTkFont(family=current_font_family, size=current_font_size, weight='bold'))
            if text_property.actual()['weight'] == 'bold':
                self.textbox.configure(font=ctk.CTkFont(family=current_font_family, size=current_font_size, weight='normal'))
            
        self.bold_btn.configure(command=change_bold)

        # italic functionality
        def change_italic():
            text_property = tk.font.Font(font=self.textbox['font'])
            if text_property.actual()['slant'] == 'roman':
                self.textbox.configure(font=(current_font_family, current_font_size, 'italic'))
            if text_property.actual()['slant'] == 'italic':
                self.textbox.configure(font=(current_font_family, current_font_size, 'normal'))
            
        self.italic_btn.configure(command=change_italic)

        # underline functionality 
        def change_underline():
            text_property = tk.font.Font(font=self.textbox['font'])
            if text_property.actual()['underline'] == 0:
                self.textbox.configure(font=(current_font_family, current_font_size, 'underline'))
            if text_property.actual()['underline'] == 1:
                self.textbox.configure(font=(current_font_family, current_font_size, 'normal'))
            
        self.underline_btn.configure(command=change_underline)

        # create radiobutton frame
        # self.radiobutton_frame = ctk.CTkFrame(self)
        # self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # self.radio_var = tkinter.IntVar(value=0)
        # self.label_radio_group = ctk.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
        # self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
        # self.radio_button_1 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
        # self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
        # self.radio_button_2 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
        # self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
        # self.radio_button_3 = ctk.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
        # self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

        # create main entry and button
        # self.entry = ctk.CTkEntry(self, placeholder_text="Search")
        # self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

        # self.main_button_1 = ctk.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
        # self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        # # create slider and progressbar frame
        # self.slider_progressbar_frame = ctk.CTkFrame(self, fg_color="transparent")
        # self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        # self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        # self.seg_button_1 = ctk.CTkSegmentedButton(self.slider_progressbar_frame)
        # self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_1 = ctk.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.progressbar_2 = ctk.CTkProgressBar(self.slider_progressbar_frame)
        # self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.slider_1 = ctk.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
        # self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
        # self.slider_2 = ctk.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
        # self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
        # self.progressbar_3 = ctk.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
        # self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

        # create scrollable frame
        # self.scrollable_frame = ctk.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
        # self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
        # self.scrollable_frame.grid_columnconfigure(0, weight=1)
        # self.scrollable_frame_switches = []
        # for i in range(100):
        #     switch = ctk.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
        #     switch.grid(row=i, column=0, padx=10, pady=(0, 20))
        #     self.scrollable_frame_switches.append(switch)

        # create checkbox and switch frame
        # self.checkbox_slider_frame = ctk.CTkFrame(self)
        # self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        # self.checkbox_1 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_2 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
        # self.checkbox_3 = ctk.CTkCheckBox(master=self.checkbox_slider_frame)
        # self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

        # # set default values
        # self.sidebar_button_3.configure(state="disabled", text="Save")
        # self.checkbox_3.configure(state="disabled")
        # self.checkbox_1.select()
        # self.scrollable_frame_switches[0].select()
        # self.scrollable_frame_switches[4].select()
        # self.radio_button_3.configure(state="disabled")
        self.appearance_mode_optionemenu.set("System")
        # self.scaling_optionemenu.set("100%")
        # self.optionmenu_1.set("CTkOptionmenu")
        # self.combobox_1.set("CTkComboBox")
        # self.slider_1.configure(command=self.progressbar_2.set)
        # self.slider_2.configure(command=self.progressbar_3.set)
        # self.progressbar_1.configure(mode="indeterminnate")
        # self.progressbar_1.start()
        # self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
        # self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
        # self.seg_button_1.set("Value 2")

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
