import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import yt_dlp
import threading
import json
import os
from settings import open_settings

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(BASE_DIR, 'settings.json'), 'r') as settings_file:
    settings = json.load(settings_file)

def download(link, quality):
    with open(os.path.join(BASE_DIR, 'settings.json'), 'r') as settings_file:
        current_settings = json.load(settings_file)
        
    output_path = current_settings["output_folder"]
    os.makedirs(output_path, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': quality,
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        CTkMessagebox(title="Completato", message="Download terminato con successo!", icon="check", width=400)
    except Exception as e:
        CTkMessagebox(title="Errore", message=f"Errore durante il download: {e}", icon="cancel", width=400)

def on_download(link_input, quality_var):
    link = link_input.get()
    quality = quality_var.get()

    if link == "":
        CTkMessagebox(title="Attenzione", message="Inserisci un link valido!", icon="warning")
        return

    thread = threading.Thread(target=download, args=(link, quality), daemon=True)
    thread.start()

def main():
    app = ctk.CTk()
    
    screen_w = app.winfo_screenwidth()
    screen_h = app.winfo_screenheight()
    scale_factor = min(screen_w / 1920, screen_h / 1080) if screen_w > 0 and screen_h > 0 else 1
    
    ctk.set_window_scaling(scale_factor)
    ctk.set_widget_scaling(scale_factor)
    
    app.title("YT MP3 Downloader - By kerlo")
    
    width = 700
    height = 380
    x = (screen_w - int(width * scale_factor)) // 2
    y = (screen_h - int(height * scale_factor)) // 2
    app.geometry(f"{width}x{height}+{x}+{y}")
    app.resizable(False, False)
    
    title_font = ctk.CTkFont(family="Segoe UI", size=20, weight="bold")
    normal_font = ctk.CTkFont(family="Segoe UI", size=13)
    
    app.columnconfigure(0, weight=1)
    app.rowconfigure(0, weight=1)
    app.rowconfigure(5, weight=1)

    title_label = ctk.CTkLabel(app, text="YouTube MP3 Downloader", font=title_font)
    title_label.grid(row=1, column=0, pady=(10, 20))

    input_frame = ctk.CTkFrame(app, fg_color="transparent")
    input_frame.grid(row=2, column=0, pady=(0, 15))

    link_input = ctk.CTkEntry(input_frame, placeholder_text="Inserisci il link del video/playlist", font=normal_font, width=280)
    link_input.pack(side="left", padx=(0, 10))

    download_btn = ctk.CTkButton(input_frame, text="Download", width=90, font=normal_font, command=lambda: on_download(link_input, quality_var))
    download_btn.pack(side="left")

    quality_frame = ctk.CTkFrame(app, fg_color="transparent")
    quality_frame.grid(row=3, column=0, pady=(0, 20))

    quality_label = ctk.CTkLabel(quality_frame, text="Qualità:", font=normal_font)
    quality_label.pack(side="left", padx=(0, 8))

    quality_var = ctk.StringVar(value=settings['default_quality'])
    quality_menu = ctk.CTkOptionMenu(quality_frame, values=["128", "192", "256", "320"], variable=quality_var, font=normal_font, width=90)
    quality_menu.pack(side="left")

    settings_btn = ctk.CTkButton(app, text="Impostazioni", width=110, font=normal_font, fg_color="gray30", hover_color="gray20", command=lambda: open_settings(app))
    settings_btn.grid(row=4, column=0, pady=(0, 10))

    app.mainloop()

if __name__ == "__main__":
    main()