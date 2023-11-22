import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [cx_Freeze.Executable("photon.py", base=base, icon="icons/photon.ico")]

cx_Freeze.setup(
    name = "Photon Text Editor",
    options = {"build_exe": {"packages":["os", "tkinter", "customtkinter", "webbrowser", "googletrans", "gtts", "playsound", "fpdf"], "include_files":["icons/photon.ico", 'icons']}},
    version = "1.6.0",
    description = "A modern responsive minimal GUI-based text editor with minimal features",
    url = "https://photontexteditor.github.io",
    executables = executables
    )
