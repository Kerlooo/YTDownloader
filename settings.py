import customtkinter as ctk
import json
import os
from tkinter import filedialog

def open_settings(app):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    with open(os.path.join(BASE_DIR, 'settings.json'), 'r') as f:
        settings = json.load(f)

    window = ctk.CTkToplevel(app)
    window.title("Settings")
    
    window.geometry("450x300")
    window.resizable(False, False)
    window.after(100, window.grab_set)

    bold_font = ctk.CTkFont(family="Segoe UI", size=14, weight="bold")
    normal_font = ctk.CTkFont(family="Segoe UI", size=14)

    window.columnconfigure(0, weight=1)

    folder_label = ctk.CTkLabel(window, text="Cartella di destinazione:", font=bold_font)
    folder_label.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")

    folder_frame = ctk.CTkFrame(window, fg_color="transparent")
    folder_frame.grid(row=1, column=0, padx=20, sticky="ew")
    folder_frame.columnconfigure(0, weight=1)

    folder_entry = ctk.CTkEntry(folder_frame, font=normal_font)
    folder_entry.insert(0, settings["output_folder"])
    folder_entry.grid(row=0, column=0, padx=(0, 10), sticky="ew")

    def browse():
        folder = filedialog.askdirectory()
        if folder:
            folder_entry.delete(0, "end")
            folder_entry.insert(0, folder)

    browse_btn = ctk.CTkButton(folder_frame, text="Sfoglia", width=80, font=normal_font, command=browse)
    browse_btn.grid(row=0, column=1)

    quality_label = ctk.CTkLabel(window, text="Qualità predefinita:", font=bold_font)
    quality_label.grid(row=2, column=0, padx=20, pady=(20, 5), sticky="w")

    quality_var = ctk.StringVar(value=settings["default_quality"])
    quality_menu = ctk.CTkOptionMenu(window, values=["128", "192", "256", "320"], variable=quality_var, font=normal_font, width=100)
    quality_menu.grid(row=3, column=0, padx=20, sticky="w")

    def save():
        settings["output_folder"] = folder_entry.get()
        settings["default_quality"] = quality_var.get()
        with open(os.path.join(BASE_DIR, 'settings.json'), 'w') as f:
            json.dump(settings, f, indent=2)
        window.destroy()

    save_btn = ctk.CTkButton(window, text="Salva", font=bold_font, width=120, command=save)
    save_btn.grid(row=4, column=0, pady=(30, 20))