import os
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import font, colorchooser, filedialog, messagebox
import customtkinter
from PIL import Image

# appearance mode
customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"

# text editor class/blueprint
class Photon(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # text editor title and geometry
        self.iconbitmap("icons/photon.ico")
        self.title("Photon Text Editor")
        self.minsize(600,600)
        self.state("zoomed")
        self.geometry("1920x1080")

        # row configure and column configure
        self.grid_rowconfigure((0, 1, 2), weight=1)
        self.grid_columnconfigure(0, weight=1)

        # menu for cascading in top
        self.main_menu = tk.Menu()

        # file icons
        new_icon = tk.PhotoImage(file='icons/new.png')
        open_icon = tk.PhotoImage(file='icons/open.png')
        save_icon = tk.PhotoImage(file='icons/save.png')
        save_as_icon = tk.PhotoImage(file='icons/save_as.png')
        exit_icon = tk.PhotoImage(file='icons/exit.png')

        self.file = tk.Menu(self.main_menu, tearoff=False)

        # # edit icons 
        copy_icon = tk.PhotoImage(file='icons/copy.png')
        paste_icon = tk.PhotoImage(file='icons/paste.png')
        cut_icon = tk.PhotoImage(file='icons/cut.png')
        clear_all_icon = tk.PhotoImage(file='icons/clear_all.png')
        find_icon = tk.PhotoImage(file='icons/find.png')

        self.edit = tk.Menu(self.main_menu, tearoff=False)

        # # view icons 
        tool_bar_icon = tk.PhotoImage(file='icons/tool_bar.png')
        status_bar_icon = tk.PhotoImage(file='icons/status_bar.png')
        
        self.view = tk.Menu(self.main_menu, tearoff=False)

        # format icons
        self.format = tk.Menu(self.main_menu, tearoff=False)

        # help icons
        self.help = tk.Menu(self.main_menu, tearoff=False)

        # color theme 
        light_default_icon = tk.PhotoImage(file='icons/light_default.png')
        light_plus_icon = tk.PhotoImage(file='icons/light_plus.png')
        dark_icon = tk.PhotoImage(file='icons/dark.png')
        red_icon = tk.PhotoImage(file='icons/red.png')
        monokai_icon = tk.PhotoImage(file='icons/monokai.png')
        night_blue_icon = tk.PhotoImage(file='icons/night_blue.png')

        self.window = tk.Menu(self.main_menu, tearoff=False)

        theme_choice = tk.StringVar()
        color_icons = (light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon)

        color_dict = {
            'Light Default ' : ('#000000', '#ffffff'),
            'Light Plus' : ('#474747', '#e0e0e0'),
            'Dark' : ('#c4c4c4', '#2d2d2d'),
            'Red' : ('#2d2d2d', '#ffe8e8'),
            'Monokai' : ('#d3b774', '#474747'),
            'Night Blue' :('#ededed', '#6b9dc2')
        }

        # cascade menus
        self.main_menu.add_cascade(label='File', menu=self.file)
        self.main_menu.add_cascade(label='Edit', menu=self.edit)
        self.main_menu.add_cascade(label='View', menu=self.view)
        self.main_menu.add_cascade(label='Window', menu=self.window)
        self.main_menu.add_cascade(label='Format', menu=self.format)
        self.main_menu.add_cascade(label='Help', menu=self.help)

        # top-frame
        self.top_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.top_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        # logo
        self.logo = customtkinter.CTkLabel(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/photon.png"), size=(60, 60)), text="", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.logo.grid(row=0, column=0, padx=(20,0), pady=20)

        # logo text
        self.logo_text = customtkinter.CTkLabel(self.top_frame, text="PHOTON", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.logo_text.grid(row=0, column=1, padx=(0, 20), pady=20)

        # font-family-box
        self.font_tuple = tk.font.families()
        self.font_family = tk.StringVar()
        self.font_family_box = customtkinter.CTkComboBox(self.top_frame, width=215, state="readonly", variable=self.font_family, values=self.font_tuple,font=customtkinter.CTkFont(weight="bold"))
        self.font_family_box.set('Times New Roman')
        self.font_family_box.grid(row=0, column=2, padx=(20,0), pady=20)

        # font-size-box
        self.size_var = tk.StringVar()
        self.font_size_box = customtkinter.CTkComboBox(self.top_frame, width=85, variable=self.size_var, values=['5', '6', '7', '8', '9', '10', '11', '12', '14', '16', '18', '20', '22', '24', '26', '28', '36', '48', '72'], state="readonly",font=customtkinter.CTkFont(weight="bold"))
        self.font_size_box.set('12')
        self.font_size_box.grid(row=0, column=3, padx=10, pady=20)

        # font-color-button
        self.font_color_btn = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/color.png"), dark_image=Image.open("icons/color_light.png"), size=(18, 18)), text="", width=20)
        self.font_color_btn.grid(row=0, column=4, padx=(0, 10), pady=20)

        # bold button
        self.bold_btn = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/bold.png"), dark_image=Image.open("icons/bold_light.png"), size=(18, 18)), text="", width=20)
        self.bold_btn.grid(row=0, column=5, padx=(20, 2), pady=5)

        # italic button
        self.italic_btn = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/italic.png"), dark_image=Image.open("icons/italic_light.png"), size=(18, 18)), text="", width=20)
        self.italic_btn.grid(row=0, column=6, padx=0, pady=5)

        # underline button
        self.underline_btn = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/underline.png"), dark_image=Image.open("icons/underline_light.png"), size=(18, 18)), text="", width=20)
        self.underline_btn.grid(row=0, column=7, padx=(2, 2), pady=10)

        # overstrike button
        self.overstrike_btn = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/overstrike.png"), dark_image=Image.open("icons/overstrike_light.png"), size=(18, 18)), text="", width=20)
        self.overstrike_btn.grid(row=0, column=8, padx=(0, 10), pady=10)


        # left align button
        self.left_align = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/left_align.png"), dark_image=Image.open("icons/left_align_light.png"), size=(18, 18)), text="", width=20)
        self.left_align.grid(row=0, column=9, padx=(10, 2), pady=10)

        # center align button
        self.center_align = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/center_align.png"), dark_image=Image.open("icons/center_align_light.png"), size=(18, 18)), text="", width=20)
        self.center_align.grid(row=0, column=10, padx=0, pady=10)

        # right align button
        self.right_align = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/right_align.png"), dark_image=Image.open("icons/right_align_light.png"), size=(18, 18)), text="", width=20)
        self.right_align.grid(row=0, column=11, padx=(2, 10), pady=10)

        # search box
        self.search_box = customtkinter.CTkEntry(self.top_frame, placeholder_text="Search", font=customtkinter.CTkFont(weight="bold"))
        self.search_box.grid(row=0, column=12, padx=(20, 0), pady=20)
       

        # go button     
        self.go = customtkinter.CTkButton(self.top_frame, text="", image=customtkinter.CTkImage(light_image=Image.open("icons/search_dark.png"), dark_image=Image.open("icons/search_light.png"), size=(18, 18)), width=10, height=10)
        self.go.grid(row=0, column=13, padx=10, pady=10)



        # scaling label
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.top_frame, values=["80%", "85%", "90%", "95%", "100%", "105%", "110%"],command=self.change_scaling_event, width=90, font=customtkinter.CTkFont(weight="bold"))
        self.scaling_optionemenu.set('Scaling')
        self.scaling_optionemenu.grid(row=0, column=14, padx=(10,20), pady=10, sticky="w")

        # appearance mode
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.top_frame, values=["Light", "Dark"],command=self.change_appearance_mode_event, width=60, font=customtkinter.CTkFont(weight="bold"))
        self.appearance_mode_optionemenu.set("Theme")
        self.appearance_mode_optionemenu.grid(row=0, column=15, padx=(0,20), pady=10, sticky="w")
        
        # text-box
        self.text_box = customtkinter.CTkTextbox(self, height=650, corner_radius=0)
        self.text_box.grid(row=2, column=0, padx=10, sticky="nsew")
        self.text_box.focus()

        # character label
        self.status_bar = customtkinter.CTkLabel(self, text=f'Characters: {0}  Words: {0}', font=customtkinter.CTkFont(weight="bold"))
        self.status_bar.grid(row=3, column=0, sticky="nsew")

        # word_label = customtkinter.CTkLabel(bot_frame, text="Word:")
        # word_label.grid(row=0, column=1, sticky="nsew")

        # font family and font size function 
        current_font_family = 'Times New Roman'
        current_font_size = 12

        def change_font(event=None):
            global current_font_family
            current_font_family = self.font_family.get()
            self.text_box.configure(font=customtkinter.CTkFont(family=current_font_family, size=current_font_size))

        def change_fontsize(event=None):
            global current_font_size
            current_font_size = int(self.size_var.get())
            self.text_box.configure(font=customtkinter.CTkFont(family=current_font_family, size=current_font_size))

        self.font_family_box.configure(command=change_font)
        self.font_size_box.configure(command=change_fontsize)
        # self.font_family_box.bind("<<ComboboxSelected>>", change_font)
        # self.font_size_box.bind("<<ComboboxSelected>>", change_fontsize)

        # bold button function
        def change_bold():
            text_property = tk.font.Font(font=self.text_box.cget("font"))
            if text_property.actual()['weight'] == 'normal':
                self.text_box.configure(font=customtkinter.CTkFont(current_font_family, current_font_size, 'bold'))
            if text_property.actual()['weight'] == 'bold':
                self.text_box.configure(font=customtkinter.CTkFont(current_font_family, current_font_size, 'normal'))
            
        self.bold_btn.configure(command=change_bold)

        # italic function
        def change_italic():
            text_property = tk.font.Font(font=self.text_box.cget("font"))
            if text_property.actual()['slant'] == 'roman':
                self.text_box.configure(font=customtkinter.CTkFont(current_font_family, current_font_size, 'italic'))
            if text_property.actual()['slant'] == 'italic':
                self.text_box.configure(font=customtkinter.CTkFont(current_font_family, current_font_size, 'normal'))
            
        self.italic_btn.configure(command=change_italic)

        # underline function 
        def change_underline():
            text_property = tk.font.Font(font=self.text_box.cget("font"))
            if text_property.actual()['underline'] == 0:
                self.text_box.configure(font=(current_font_family, current_font_size, 'underline'))
            if text_property.actual()['underline'] == 1:
                self.text_box.configure(font=(current_font_family, current_font_size, 'normal'))
            
        self.underline_btn.configure(command=change_underline)

        # overstrike function 
        def change_overstrike():
            text_property = tk.font.Font(font=self.text_box.cget("font"))
            if text_property.actual()['overstrike'] == 0:
                self.text_box.configure(font=(current_font_family, current_font_size, 'overstrike'))
            if text_property.actual()['overstrike'] == 1:
                self.text_box.configure(font=(current_font_family, current_font_size, 'normal'))
            
        self.overstrike_btn.configure(command=change_overstrike)

        # font color function 
        def change_font_color():
            color_var = tk.colorchooser.askcolor()
            self.text_box.configure(text_color=color_var[1])

        self.font_color_btn.configure(command=change_font_color)

        # left align function 
        def align_left():
            text_content = self.text_box.get(1.0, 'end')
            self.text_box.tag_config('left', justify=tk.LEFT)
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.INSERT, text_content, 'left')

        self.left_align.configure(command=align_left)

        # center align function
        def align_center():
            text_content = self.text_box.get(1.0, 'end')
            self.text_box.tag_config('center', justify=tk.CENTER)
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.INSERT, text_content, 'center')

        self.center_align.configure(command=align_center)

        # right align function
        def align_right():
            text_content = self.text_box.get(1.0, 'end')
            self.text_box.tag_config('right', justify=tk.RIGHT)
            self.text_box.delete(1.0, tk.END)
            self.text_box.insert(tk.INSERT, text_content, 'right')

        self.right_align.configure(command=align_right)

        self.text_box.configure(font=customtkinter.CTkFont('Times New Roman', 12))

        # status bar
        text_changed = False 
        def changed(event=None):
            global text_changed
            if self.text_box.edit_modified():
                text_changed = True 
                words = len(self.text_box.get(1.0, 'end-1c').split())
                characters = len(self.text_box.get(1.0, 'end-1c'))
                self.status_bar.configure(text=f'Characters: {characters}  Words: {words}')
            self.text_box.edit_modified(False)

        self.text_box.bind('<<Modified>>', changed)
        # self.text_box.configure(command=changed)

        # main menu function begins
        # variable 
        url = ''

        # new file function
        def new_file(event=None):
            global url 
            url = ''
            self.text_box.delete(1.0, tk.END)

        # file commands for new
        self.file.add_command(label='New', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)

        # open file function
        def open_file(event=None):
            global url 
            url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            try:
                with open(url, 'r') as fr:
                    self.text_box.delete(1.0, tk.END)
                    self.text_box.insert(1.0, fr.read())
            except FileNotFoundError:
                return 
            except:
                return 
            app.title(os.path.basename(url))

        self.file.add_command(label='Open', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)

        # save file function
        def save_file(event=None):
            global url 
            try:
                if url:
                    content = str(self.text_box.get(1.0, tk.END))
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                else:
                    url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    content2 = self.text_box.get(1.0, tk.END)
                    url.write(content2)
                    url.close()
            except:
                return 

        self.file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command = save_file)


        # save as function 
        def save_as(event=None):
            global url 
            try:
                content = self.text_box.get(1.0, tk.END)
                url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('Python Script', '*.py'), ('C++ Script', '*.cpp'), ('C# Script', '*.cs'), ('Java Script', '*.java'), ('R Script', '*.r'), ('All files', '*.*')))
                url.write(content)
                url.close()
            except:
                return 


        self.file.add_command(label='Save As', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=save_as)

        # exit program function 
        def exit_func(event=None):
            global url, text_changed
            try:
                if text_changed:
                    mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file ?')
                    if mbox is True:
                        if url:
                            content = self.text_box.get(1.0, tk.END)
                            with open(url, 'w', encoding='utf-8') as fw:
                                fw.write(content)
                                self.destroy()
                        else:
                            content2 = str(self.text_box.get(1.0, tk.END))
                            url = filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                            url.write(content2)
                            url.close()
                            self.destroy()
                    elif mbox is False:
                        self.destroy()
                else:
                    self.destroy()
            except:
                return 
        self.file.add_command(label='Close', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_func)

        # find and replace function
        def find_func(event=None):

            def find():
                word = find_input.get()
                self.text_box.tag_remove('match', '1.0', tk.END)
                matches = 0
                if word:
                    start_pos = '1.0'
                    while True:
                        start_pos = self.text_box.search(word, start_pos, stopindex=tk.END)
                        if not start_pos:
                            break 
                        end_pos = f'{start_pos}+{len(word)}c'
                        self.text_box.tag_add('match', start_pos, end_pos)
                        matches += 1
                        start_pos = end_pos
                        self.text_box.tag_config('match', text_color='red', fg_color='yellow')
            
            def replace():
                word = find_input.get()
                replace_text = replace_input.get()
                content = self.text_box.get(1.0, tk.END)
                new_content = content.replace(word, replace_text)
                self.text_box.delete(1.0, tk.END)
                self.text_box.insert(1.0, new_content)

            find_dialogue = tk.Toplevel()
            find_dialogue.geometry('450x250+500+200')
            find_dialogue.title('Find')
            find_dialogue.resizable(0,0)

            # frame 
            find_frame = ttk.LabelFrame(find_dialogue, text='Find/Replace')
            find_frame.pack(pady=20)

            # labels
            text_find_label = ttk.Label(find_frame, text='Find : ')
            text_replace_label = ttk.Label(find_frame, text= 'Replace')

            # entry 
            find_input = ttk.Entry(find_frame, width=30)
            replace_input = ttk.Entry(find_frame, width=30)

            # find button 
            find_button = ttk.Button(find_frame, text='Find', command=find)
            replace_button = ttk.Button(find_frame, text= 'Replace', command=replace)

            # label grid 
            text_find_label.grid(row=0, column=0, padx=4, pady=4)
            text_replace_label.grid(row=1, column=0, padx=4, pady=4)

            # entry grid 
            find_input.grid(row=0, column=1, padx=4, pady=4)
            replace_input.grid(row=1, column=1, padx=4, pady=4)

            # button grid 
            find_button.grid(row=2, column=0, padx=8, pady=4)
            replace_button.grid(row=2, column=1, padx=8, pady=4)

            find_dialogue.mainloop()

        # edit commands 
        self.edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C', command=lambda : self.text_box.event_generate("<Control c>"))
        self.edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V', command=lambda : self.text_box.event_generate("<Control v>"))
        self.edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X', command=lambda : self.text_box.event_generate("<Control x>"))
        self.edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X', command= lambda : self.text_box.delete(1.0, tk.END))
        self.edit.add_command(label='Find', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F', command = find_func)

        # view check button 
        show_statusbar = tk.BooleanVar()
        show_statusbar.set(True)
        show_top_frame = tk.BooleanVar()
        show_top_frame.set(True)
        def hide_top_frame():
            global show_top_frame
            if show_top_frame:
                self.top_frame.pack_forget()
                show_top_frame = False 
            else :
                self.text_box.pack_forget()
                self.status_bar.pack_forget()
                self.top_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
                self.text_box.pack(fill=tk.BOTH, expand=True)
                self.status_bar.pack(side=tk.BOTTOM)
                show_top_frame = True 

        def hide_statusbar():
            global show_statusbar
            if show_statusbar:
                self.status_bar.pack_forget()
                show_statusbar = False 
            else :
                self.status_bar.grid(row=3, column=0, sticky="nsew")
                show_statusbar = True 


        self.view.add_checkbutton(label='Tool Bar',onvalue=True, offvalue=0,variable = show_top_frame, image=tool_bar_icon, compound=tk.LEFT, command=hide_top_frame)
        self.view.add_checkbutton(label='Status Bar',onvalue=1, offvalue=False,variable = show_statusbar, image=status_bar_icon, compound=tk.LEFT, command=hide_statusbar)

        # color theme 
        def change_theme():
            chosen_theme = theme_choice.get()
            color_tuple = color_dict.get(chosen_theme)
            fg_colour, bg_color = color_tuple[0], color_tuple[1]
            self.text_box.configure(fg_color=bg_color, text_color=fg_colour) 
        count = 0 
        for i in color_dict:
            self.window.add_radiobutton(label = i, image=color_icons[count], variable=theme_choice, compound=tk.LEFT, command=change_theme)
            count += 1 

        # main menu function ends

        self.config(menu=self.main_menu)

        # bind shortcut keys 
        self.bind("<Control-n>", new_file)
        self.bind("<Control-o>", open_file)
        self.bind("<Control-s>", save_file)
        self.bind("<Control-Alt-s>", save_as)
        self.bind("<Control-q>", exit_func)
        self.bind("<Control-f>", find_func)

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = Photon()
    app.mainloop()
