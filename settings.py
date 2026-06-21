import customtkinter as ctk
import json
import os
from tkinter import filedialog
from translations import t, LANGUAGES, DEFAULT_LANG

def open_settings(app, on_save=None):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    with open(os.path.join(BASE_DIR, 'settings.json'), 'r') as f:
        settings = json.load(f)

    lang = settings.get("language", DEFAULT_LANG)
    code_to_name = {code: name for name, code in LANGUAGES.items()}

    window = ctk.CTkToplevel(app)
    window.title(t(lang, "settings_window_title"))
    window.after(100, window.grab_set)

    bold_font = ctk.CTkFont(family="Segoe UI", size=14, weight="bold")
    normal_font = ctk.CTkFont(family="Segoe UI", size=14)

    window.columnconfigure(0, weight=1)

    folder_label = ctk.CTkLabel(window, text=t(lang, "folder_label"), font=bold_font)
    folder_label.grid(row=0, column=0, padx=20, pady=(20, 5), sticky="w")

    folder_frame = ctk.CTkFrame(window, fg_color="transparent")
    folder_frame.grid(row=1, column=0, padx=20, sticky="ew")
    folder_frame.columnconfigure(0, weight=1)

    folder_entry = ctk.CTkEntry(folder_frame, font=normal_font, width=280)
    folder_entry.insert(0, settings["output_folder"])
    folder_entry.grid(row=0, column=0, padx=(0, 10), sticky="ew")

    def browse():
        folder = filedialog.askdirectory()
        if folder:
            folder_entry.delete(0, "end")
            folder_entry.insert(0, folder)

    browse_btn = ctk.CTkButton(folder_frame, text=t(lang, "browse_btn"), width=80, font=normal_font, command=browse)
    browse_btn.grid(row=0, column=1)

    quality_label = ctk.CTkLabel(window, text=t(lang, "default_quality_label"), font=bold_font)
    quality_label.grid(row=2, column=0, padx=20, pady=(20, 5), sticky="w")

    quality_var = ctk.StringVar(value=settings["default_quality"])
    quality_menu = ctk.CTkOptionMenu(window, values=["128", "192", "256", "320"], variable=quality_var, font=normal_font, width=100)
    quality_menu.grid(row=3, column=0, padx=20, sticky="w")

    language_label = ctk.CTkLabel(window, text=t(lang, "language_label"), font=bold_font)
    language_label.grid(row=4, column=0, padx=20, pady=(20, 5), sticky="w")

    language_var = ctk.StringVar(value=code_to_name.get(lang, code_to_name[DEFAULT_LANG]))
    language_menu = ctk.CTkOptionMenu(window, values=list(LANGUAGES.keys()), variable=language_var, font=normal_font, width=150)
    language_menu.grid(row=5, column=0, padx=20, sticky="w")

    def save():
        settings["output_folder"] = folder_entry.get()
        settings["default_quality"] = quality_var.get()
        settings["language"] = LANGUAGES[language_var.get()]
        with open(os.path.join(BASE_DIR, 'settings.json'), 'w') as f:
            json.dump(settings, f, indent=2)
        window.destroy()
        if on_save:
            on_save(settings)

    save_btn = ctk.CTkButton(window, text=t(lang, "save_btn"), font=bold_font, width=120, command=save)
    save_btn.grid(row=6, column=0, pady=(30, 20))

    window.update_idletasks()
    width = window.winfo_reqwidth() + 40
    height = window.winfo_reqheight() + 20
    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()
    x = (screen_w - width) // 2
    y = (screen_h - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")
    window.resizable(False, False)
