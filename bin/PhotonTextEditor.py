import os 
#importing os module 
import tkinter as tk 
#importing tkinter module as tk
from tkinter import * 
#importing all from tkinter
from tkinter import ttk 
#importing ttk from tkinter
from tkinter import font, colorchooser, filedialog, messagebox
import customtkinter 
#importing customtkinter
from PIL import Image 
#importing Image from pillow library
import webbrowser 
#for documentation link 
from googletrans import Translator 
#for translation
import gtts 
#for text to speech
from playsound import playsound 
#for playing sound
# from fpdf import FPDF 
# #for converting text to pdf

# appearance mode
customtkinter.set_appearance_mode("Dark")  
# Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  
# Themes: "blue" (standard), "green", "dark-blue"

# text editor class/blueprint
class Photon(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        # using super method to inherit all the attributes of base class to derived class

        # text editor title and geometry
        self.iconbitmap("icons/photon.ico")
        self.title("Photon Text Editor")
        self.minsize(1400,770)
        self.state("zoomed")
        self.geometry("1920x1080")

        # row configure and column configure (3x1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # menu for cascading in top
        self.main_menu = tk.Menu(self)
        self.config(menu=self.main_menu)


        # file icons
        new_icon = tk.PhotoImage(file='icons/new_icon.png')
        open_icon = tk.PhotoImage(file='icons/open_icon.png')
        save_icon = tk.PhotoImage(file='icons/save_icon.png')
        save_as_icon = tk.PhotoImage(file='icons/saveas_icon.png')
        exit_icon = tk.PhotoImage(file='icons/exit_icon.png')
        export_icon = tk.PhotoImage(file='icons/exportas_icon.png')

        self.file = tk.Menu(self.main_menu, tearoff=False)

        # edit icons 
        select_icon = tk.PhotoImage(file='icons/select_icon.png')
        deselect_icon = tk.PhotoImage(file='icons/deselect_icon.png')
        copy_icon = tk.PhotoImage(file='icons/copy_icon.png')
        paste_icon = tk.PhotoImage(file='icons/paste_icon.png')
        cut_icon = tk.PhotoImage(file='icons/cut_icon.png')
        clear_all_icon = tk.PhotoImage(file='icons/clearall_icon.png')
        find_icon = tk.PhotoImage(file='icons/find_icon.png')

        self.edit = tk.Menu(self.main_menu, tearoff=False)

        # view icons 
        
        self.view = tk.Menu(self.main_menu, tearoff=False)

        # tools icons
        self.tools = tk.Menu(self.main_menu, tearoff=False)

        # format icons
        self.format = tk.Menu(self.main_menu, tearoff=False)

        # help icons
        self.help = tk.Menu(self.main_menu, tearoff=False)

        # window icons

        # color theme 
        self.window = tk.Menu(self.main_menu, tearoff=False)

        # color palettes for text box
        theme_choice = tk.StringVar()

        color_dict = {
            ' Light+' : ('#474747', '#e0e0e0'),
            ' Dark' : ('#c4c4c4', '#2d2d2d'),
            ' Light' : ('#000000', '#ffffff'),
            ' Night Blue' :('#ededed', '#6b9dc2'),
            ' Red' : ('#2d2d2d', '#ffe8e8'),
            ' Monokai' : ('#d3b774', '#474747')
        }

        # cascade menus
        self.main_menu.add_cascade(label='File', menu=self.file)
        self.main_menu.add_cascade(label='Edit', menu=self.edit)
        self.main_menu.add_cascade(label='View', menu=self.view)
        self.main_menu.add_cascade(label='Window', menu=self.window)
        self.main_menu.add_cascade(label='Tools', menu=self.tools)
        self.main_menu.add_cascade(label='Format', menu=self.format)
        self.main_menu.add_cascade(label='Help', menu=self.help)

        # top-frame
        self.top_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.top_frame.grid(row=0, column=0, sticky="nsew", padx=0, pady=0)
        self.top_frame.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14), weight=1)
        # self.top_frame.pack(side=tk.TOP, fill=tk.X)

        # logo image
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
        self.font_size_box.grid(row=0, column=3, padx=(3, 3), pady=20)

        # font-color-button
        self.font_color_btn = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/color.png"), dark_image=Image.open("icons/color_light.png"), size=(18, 18)), text="", width=20)
        self.font_color_btn.grid(row=0, column=4, padx=(0, 20), pady=20)

        # bold button
        self.bold_btn = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/bold.png"), dark_image=Image.open("icons/bold_light.png"), size=(18, 18)), text="", width=20)
        self.bold_btn.grid(row=0, column=5, padx=(20, 0), pady=5)

        # italic button
        self.italic_btn = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/italic.png"), dark_image=Image.open("icons/italic_light.png"), size=(18, 18)), text="", width=20)
        self.italic_btn.grid(row=0, column=6, padx=(3, 3), pady=5)

        # underline button
        self.underline_btn = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/underline.png"), dark_image=Image.open("icons/underline_light.png"), size=(18, 18)), text="", width=20)
        self.underline_btn.grid(row=0, column=7, padx=(0, 3), pady=10)

        # overstrike button
        self.overstrike_btn = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/overstrike.png"), dark_image=Image.open("icons/overstrike_light.png"), size=(18, 18)), text="", width=20)
        self.overstrike_btn.grid(row=0, column=8, padx=(0, 20), pady=10)

        # left align button
        self.left_align = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/left_align.png"), dark_image=Image.open("icons/left_align_light.png"), size=(18, 18)), text="", width=20)
        self.left_align.grid(row=0, column=9, padx=(20, 3), pady=10)

        # center align button
        self.center_align = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/center_align.png"), dark_image=Image.open("icons/center_align_light.png"), size=(18, 18)), text="", width=20)
        self.center_align.grid(row=0, column=10, padx=0, pady=10)

        # right align button
        self.right_align = customtkinter.CTkButton(self.top_frame, image=customtkinter.CTkImage(light_image=Image.open("icons/right_align.png"), dark_image=Image.open("icons/right_align_light.png"), size=(18, 18)), text="", width=20)
        self.right_align.grid(row=0, column=11, padx=(3, 20), pady=10)

        # search box
        self.search_box = customtkinter.CTkEntry(self.top_frame, placeholder_text="Search", font=customtkinter.CTkFont(weight="bold"))
        self.search_box.grid(row=0, column=12, padx=(20, 0), pady=20)

        def search():
            fword = self.search_box.get()
            self.text_box.tag_remove('match', '1.0', tk.END)
            matches = 0
            if fword:
                start_pos = '0.0'
                while True:
                    start_pos = self.text_box.search(fword, start_pos, stopindex=tk.END)
                    if not start_pos:
                        break 
                    end_pos = f'{start_pos}+{len(fword)}c'
                    self.text_box.tag_add('match', start_pos, end_pos)
                    matches += 1
                    start_pos = end_pos
                    self.text_box.tag_config('match', foreground='blue', background='white')

        # go button     
        self.go = customtkinter.CTkButton(self.top_frame, text="", image=customtkinter.CTkImage(light_image=Image.open("icons/search_dark.png"), dark_image=Image.open("icons/search_light.png"), size=(18, 18)), width=10, command=search)
        self.go.grid(row=0, column=13, padx=(3, 20), pady=10)

        # scaling label
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.top_frame, values=["80%", "85%", "90%", "95%", "100%", "105%"],command=self.change_scaling_event, width=90, font=customtkinter.CTkFont(weight="bold"))
        self.scaling_optionemenu.set('Scaling')
        self.scaling_optionemenu.grid(row=0, column=14, padx=(20, 20), pady=10, sticky="w")

        # appearance mode
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.top_frame, values=["Light", "Dark"],command=self.change_appearance_mode_event, width=60, font=customtkinter.CTkFont(weight="bold"))
        self.appearance_mode_optionemenu.set("Theme")
        self.appearance_mode_optionemenu.grid(row=0, column=15, padx=(0,20), pady=10)

        # center frame
        self.center_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.center_frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        self.center_frame.grid_columnconfigure(0, weight=1)
        self.center_frame.grid_rowconfigure(0, weight=1)
        # self.center_frame.pack(fill=tk.BOTH, expand=True)

        # text-box
        self.text_box = customtkinter.CTkTextbox(self.center_frame, corner_radius=0, height=650)
        self.text_box.grid(row=0, column=0, sticky="nsew")
        # self.text_box.pack(fill=tk.BOTH, expand=True)
        self.text_box.focus()

        # bottom frame
        self.bottom_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.bottom_frame.grid(row=2, column=0, sticky="nsew", padx=0, pady=0)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_rowconfigure(0, weight=1)
        # self.bottom_frame.pack(side=tk.BOTTOM)

        # status bar
        (line, col)= self.text_box.index(tk.CURRENT).split(".")
        self.status_bar = customtkinter.CTkLabel(self.bottom_frame, text=f'Characters: {0}  Words: {0}\tUTF-8\tLn {line}, Col {col}', font=customtkinter.CTkFont(weight="bold"))
        # self.status_bar.grid(row=0, column=0, sticky="nsew")
        self.status_bar.pack(side=tk.BOTTOM)

        # font family and font size function 
        current_font_family = 'Times New Roman'
        current_font_size = 12

        def change_font(event=None):
            nonlocal current_font_family
            current_font_family = self.font_family.get()
            self.text_box.configure(font=customtkinter.CTkFont(family=current_font_family, size=current_font_size))

        def change_fontsize(event=None):
            nonlocal current_font_size
            current_font_size = int(self.size_var.get())
            self.text_box.configure(font=customtkinter.CTkFont(family=current_font_family, size=current_font_size))

        self.font_family_box.configure(command=change_font)
        self.font_size_box.configure(command=change_fontsize)

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
                self.text_box.configure(font=customtkinter.CTkFont(current_font_family, current_font_size, slant='italic'))
            if text_property.actual()['slant'] == 'italic':
                self.text_box.configure(font=customtkinter.CTkFont(current_font_family, current_font_size, slant='roman'))    
            
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
            nonlocal text_changed
            if self.text_box.edit_modified():
                text_changed = True 
                words = len(self.text_box.get(1.0, 'end-1c').split())
                characters = len(self.text_box.get(1.0, 'end-1c'))
                (line, col)= self.text_box.index(tk.CURRENT).split(".")
                self.status_bar.configure(text=f'Characters: {characters}  Words: {words}\tUTF-8\tLn {line}, Col {col}')
            self.text_box.edit_modified(False)

        self.text_box.bind('<<Modified>>', changed)

        # main menu function begins
        url = ''

        # new file function
        def new_file(event=None):
            nonlocal url 
            url = ''
            self.text_box.delete(1.0, tk.END)

        # file commands for new
        self.file.add_command(label='New...', image=new_icon, compound=tk.LEFT, accelerator='Ctrl+N', command=new_file)

        # open file function
        def open_file(event=None):
            nonlocal url 
            url = customtkinter.filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            try:
                with open(url, 'r') as fr:
                    self.text_box.delete(1.0, tk.END)
                    self.text_box.insert(1.0, fr.read())
            except FileNotFoundError:
                return 
            except:
                return 
            app.title(os.path.basename(url))

        self.file.add_command(label='Open...', image=open_icon, compound=tk.LEFT, accelerator='Ctrl+O', command=open_file)

        # save file function
        def save_file(event=None):
            nonlocal url 
            try:
                if url:
                    content = str(self.text_box.get(1.0, tk.END))
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                else:
                    url = customtkinter.filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    content2 = self.text_box.get(1.0, tk.END)
                    url.write(content2)
                    url.close()
            except:
                return 

        self.file.add_command(label='Save', image=save_icon, compound=tk.LEFT, accelerator='Ctrl+S', command = save_file)


        # save as function 
        def save_as(event=None):
            nonlocal url 
            try:
                content = self.text_box.get(1.0, tk.END)
                url = customtkinter.filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('Python Script', '*.py'), ('C++ Script', '*.cpp'), ('C# Script', '*.cs'), ('Java Script', '*.java'), ('R Script', '*.r'), ('All files', '*.*')))
                url.write(content)
                url.close()
            except:
                return 


        self.file.add_command(label='Save As...', image=save_as_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+S', command=save_as)

        # export as function
        self.file.add_command(label='Export As', image=export_icon, compound=tk.LEFT, state=tk.DISABLED)


        # exit file function 
        def exit_func(event=None):
            nonlocal url, text_changed
            try:
                if text_changed:
                    mbox = tk.messagebox.askyesnocancel('Warning', 'Do you want to save the file?')
                    if mbox is True:
                        if url:
                            content = self.text_box.get(1.0, tk.END)
                            with open(url, 'w', encoding='utf-8') as fw:
                                fw.write(content)
                                self.destroy()
                        else:
                            content2 = str(self.text_box.get(1.0, tk.END))
                            url = tk.filedialog.asksaveasfile(mode = 'w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                            url.write(content2)
                            url.close()
                            self.destroy()
                    elif mbox is False:
                        self.destroy()
                else:
                    self.destroy()
            except:
                return 
        self.file.add_separator() 
        self.file.add_command(label='Exit', image=exit_icon, compound=tk.LEFT, accelerator='Ctrl+Q', command=exit_func)

        # find and replace function
        def find_func(event=None):

            def find():
                word = find_input.get()
                self.text_box.tag_remove('match', '1.0', tk.END)
                matches = 0
                if word:
                    start_pos = '0.0'
                    while True:
                        start_pos = self.text_box.search(word, start_pos, stopindex=tk.END)
                        if not start_pos:
                            break 
                        end_pos = f'{start_pos}+{len(word)}c'
                        self.text_box.tag_add('match', start_pos, end_pos)
                        matches += 1
                        start_pos = end_pos
                        self.text_box.tag_config('match', foreground='blue', background='white')

            def replace():
                word = find_input.get()
                replace_text = replace_input.get()
                content = self.text_box.get(1.0, tk.END)
                new_content = content.replace(word, replace_text)
                self.text_box.delete(1.0, tk.END)
                self.text_box.insert(1.0, new_content)

            find_dialogue = customtkinter.CTkToplevel()
            find_dialogue.geometry('450x150+500+200')
            find_dialogue.title('Find/Replace')
            find_dialogue.resizable(0,0)

            # frame 
            find_frame = customtkinter.CTkFrame(find_dialogue)
            find_frame.pack(pady=20)

            # labels
            text_find_label = customtkinter.CTkLabel(find_frame, text='Find : ')
            text_replace_label = customtkinter.CTkLabel(find_frame, text= 'Replace :')

            # entry 
            find_input = customtkinter.CTkEntry(find_frame, width=150)
            find_input.focus()
            replace_input = customtkinter.CTkEntry(find_frame, width=150)

            # find button 
            find_button = customtkinter.CTkButton(find_frame, text='Find', command=find, width=50)
            replace_button = customtkinter.CTkButton(find_frame, text= 'Replace', command=replace, width=50)

            # label grid 
            text_find_label.grid(row=0, column=0, padx=4, pady=4)
            text_replace_label.grid(row=1, column=0, padx=4, pady=4)

            # entry grid 
            find_input.grid(row=0, column=1, padx=4, pady=4)
            replace_input.grid(row=1, column=1, padx=4, pady=4)

            # button grid 
            find_button.grid(row=2, column=0, padx=8, pady=4, sticky="w")
            replace_button.grid(row=2, column=1, padx=8, pady=4, sticky="e")

        # edit commands 
        self.edit.add_command(label='Select', image=select_icon, compound=tk.LEFT, accelerator='Ctrl+C', command=lambda : self.text_box.event_generate("<Control a>"), state=tk.DISABLED)
        self.edit.add_command(label='Deselect', image=deselect_icon, compound=tk.LEFT, accelerator='Ctrl+C', command=lambda : self.text_box.event_generate("<Control d>"), state=tk.DISABLED)
        self.edit.add_command(label='Copy', image=copy_icon, compound=tk.LEFT, accelerator='Ctrl+C', command=lambda : self.text_box.event_generate("<Control c>"))
        self.edit.add_command(label='Paste', image=paste_icon, compound=tk.LEFT, accelerator='Ctrl+V', command=lambda : self.text_box.event_generate("<Control v>"))
        self.edit.add_command(label='Cut', image=cut_icon, compound=tk.LEFT, accelerator='Ctrl+X', command=lambda : self.text_box.event_generate("<Control x>"))
        self.edit.add_command(label='Clear All', image=clear_all_icon, compound=tk.LEFT, accelerator='Ctrl+Alt+X', command= lambda : self.text_box.delete(1.0, tk.END))
        self.edit.add_command(label='Find/Replace', image=find_icon, compound=tk.LEFT, accelerator='Ctrl+F', command = find_func)

        # view menu commands 
        # color theme 
        color_theme = tk.PhotoImage(file='icons/colortheme_icon.png')
        keyboard_shortcut = tk.PhotoImage(file='icons/keyboardshortcut_icon.png')
        self.color_theme = tk.Menu(self.view, tearoff=0)

        def change_theme():
            chosen_theme = theme_choice.get()
            color_tuple = color_dict.get(chosen_theme)
            fg_colour, bg_color = color_tuple[0], color_tuple[1]
            self.text_box.configure(fg_color=bg_color, text_color=fg_colour) 
        count = 0 
        for i in color_dict:
            self.color_theme.add_radiobutton(label = i, variable=theme_choice, compound=tk.LEFT, command=change_theme) #image=color_icons[count]
            count += 1 
        
        self.view.add_cascade(label='Color Theme', image=color_theme, menu=self.color_theme, compound=tk.LEFT)
        self.view.add_cascade(label="Keyboard Shortcuts", image=keyboard_shortcut, compound=tk.LEFT)

        # view check button
        show_statusbar = tk.BooleanVar()
        show_statusbar.set(True)
        show_top_frame = tk.BooleanVar()
        show_top_frame.set(True)
        def hide_top_frame():
            nonlocal show_top_frame
            if show_top_frame:
                self.top_frame.grid_forget()
                show_top_frame = False 
            else :
                self.text_box.grid_forget()
                self.status_bar.grid_forget()
                self.top_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
                self.text_box.pack(fill=tk.BOTH, expand=True)
                self.status_bar.pack(side=tk.BOTTOM)
                show_top_frame = True 

        def hide_statusbar():
            nonlocal show_statusbar
            if show_statusbar:
                self.bottom_frame.grid_forget()
                show_statusbar = False 
            else :
                self.bottom_frame.grid(row=3, column=0, sticky="nsew")
                # self.status_bar.pack(side=tk.BOTTOM)
                show_statusbar = True 


        self.view.add_checkbutton(label=' Tool Bar',onvalue=True, offvalue=0,variable = show_top_frame, compound=tk.LEFT, command=hide_top_frame)
        self.view.add_checkbutton(label=' Status Bar',onvalue=1, offvalue=False,variable = show_statusbar, compound=tk.LEFT, command=hide_statusbar)

        # tools commands
        translate_icon = tk.PhotoImage(file='icons/translate_icon.png')
        speech_icon = tk.PhotoImage(file='icons/texttospeech_icon.png')

        self.tools.add_command(label='Translate (ne)', image=translate_icon, compound=tk.LEFT, command = self.open_input_dialog_event)
        self.tools.add_command(label='Text to Speech (en)', image=speech_icon, compound=tk.LEFT, command = self.texttospeech)

        # format commands
        # font menu
        font_family_icon = tk.PhotoImage(file='icons/font_family_icon.png')
        font_align_icon = tk.PhotoImage(file='icons/text_align_icon.png')
        font_style_icon = tk.PhotoImage(file='icons/font_style_icon.png')
        self.font_menu = tk.Menu(self.view, tearoff=0)
        count = 0 
        for i in list(self.font_tuple):
            self.font_menu.add_radiobutton(label = " "+i, variable=self.font_family, compound=tk.LEFT, command=change_font) #image=color_icons[count]
            count += 1
        self.format.add_cascade(label='Font Family', image=font_family_icon, menu=self.font_menu, compound=tk.LEFT)

        # font align
        self.align_menu = tk.Menu(self.view, tearoff=0)
        self.align_menu.add_radiobutton(label = " Left", compound=tk.LEFT, command=align_left)
        self.align_menu.add_radiobutton(label = " Center", compound=tk.LEFT, command=align_center)
        self.align_menu.add_radiobutton(label = " Right", compound=tk.LEFT, command=align_right)
        self.format.add_cascade(label='Font Align', image=font_align_icon, menu=self.align_menu, compound=tk.LEFT)
        
        # font style
        self.style_menu = tk.Menu(self.view, tearoff=0)
        self.style_menu.add_radiobutton(label = " Bold", compound=tk.LEFT, command=change_bold)
        self.style_menu.add_radiobutton(label = " Italic", compound=tk.LEFT, command=change_italic)
        self.style_menu.add_radiobutton(label = " Underline", compound=tk.LEFT, command=change_underline)
        self.style_menu.add_radiobutton(label = " Overstrike", compound=tk.LEFT, command=change_overstrike)
        self.format.add_cascade(label='Font Style', image=font_style_icon, menu=self.style_menu, compound=tk.LEFT)


        # help commands
        self.help.add_command(label='Welcome', compound=tk.LEFT, command = lambda : tk.messagebox.showinfo(title="Welcome", message="Welcome to Photon! Your're using v1.4.0"))
        self.help.add_command(label='About Photon', compound=tk.LEFT, command = lambda : tk.messagebox.showinfo(title="About Photon", message="Photon Text Editor v1.4.0\nPowered by Python"))
        self.help.add_separator()
        self.help.add_command(label='View License', compound=tk.LEFT, command = lambda : webbrowser.open_new_tab("https://github.com/photontexteditor/Photon/blob/main/LICENSE"))
        
        self.help.add_command(label='Privacy Statement', compound=tk.LEFT, command = lambda : webbrowser.open_new_tab("https://github.com/photontexteditor/Photon/blob/main/SECURITY.md"))

        self.help.add_separator()
        self.help.add_command(label='Show Release Notes', compound=tk.LEFT, command = lambda : webbrowser.open_new_tab("https://github.com/photontexteditor/Photon/releases"))
        self.help.add_command(label='Report Issue', compound=tk.LEFT, command = lambda : webbrowser.open_new_tab('https://github.com/photontexteditor/Photon/blob/main/CONTRIBUTING.md'))
        self.help.add_command(label='Documentation', compound=tk.LEFT, command = lambda : webbrowser.open_new_tab("https://www.github.com/photontexteditor/Photon"))

        # window menu
        minimize_icon = tk.PhotoImage(file='icons/minimize_icon.png')

        def hide_window(event=None):
            self.iconify()

        self.window.add_command(label='Minimize', image=minimize_icon, compound=tk.LEFT, accelerator="Control+M", command=hide_window)

        # main menu function ends

        # bind shortcut keys 
        self.bind("<Control-m>", hide_window)
        self.bind("<Control-n>", new_file)
        self.bind("<Control-o>", open_file)
        self.bind("<Control-s>", save_file)
        self.bind("<Control-Alt-s>", save_as)
        self.bind("<Control-q>", exit_func)
        self.bind("<Control-f>", find_func)

    def open_input_dialog_event(self):
        trans_catch = self.text_box.get(1.0, tk.END)
        if trans_catch !="\n":
            self.translator = Translator()
            translated_text = self.translator.translate(trans_catch, dest='ne')
            dialog = customtkinter.CTkToplevel()
            dialog.geometry('450x150+500+200')
            dialog.title('Translate (ne)')
            dialog.resizable(0,0)
          
            # frame 
            dialog_frame = customtkinter.CTkFrame(dialog)
            dialog_frame.pack(pady=40)
           
            # labels
            dialog_label = customtkinter.CTkLabel(dialog_frame, text=translated_text.text, font=customtkinter.CTkFont(size=20, weight="bold"))
            dialog_label.grid(row=0, column=0, padx=4, pady=4)
   
    def texttospeech(self):
        text_catch = self.text_box.get(1.0, tk.END)
        if text_catch!="\n":
            text_speech = gtts.gTTS(text_catch, lang='en', slow=False)
            # give folder path
            text_speech.save("speech.mp3")
            dialog = customtkinter.CTkToplevel()
            dialog.geometry('450x150+500+200')
            dialog.title('Text to Speech (en)')
            dialog.resizable(0,0)
            
            # frame 
            dialog_frame = customtkinter.CTkFrame(dialog)
            dialog_frame.pack(pady=40)
           
            # labels
            dialog_label = customtkinter.CTkButton(dialog_frame, text="Play", font=customtkinter.CTkFont(weight="bold"), command=lambda : playsound("speech.mp3"))
            dialog_label.grid(row=0, column=0, padx=4, pady=4)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = Photon()
    app.mainloop()
