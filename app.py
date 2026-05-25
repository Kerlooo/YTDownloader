import customtkinter as ctk
import yt_dlp
import threading
import json
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

with open('settings.json', 'r') as settings_file:
    settings = json.load(settings_file)

def download(link, quality):

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(settings["output_folder"], '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': quality,
        }],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])

def on_download():
    link = link_input.get()
    quality = quality_var.get()

    if link == "":
        print("Insert un link!")
        return

    thread = threading.Thread(target=download, args=(link, quality), daemon=True)
    thread.start()

def main():
    app = ctk.CTk()
    app.title("YT MP3 Downloader - By kerlo")
    app.geometry("600x400")
    app.resizable(False, False)

    app.columnconfigure(0, weight = 1)

    global link_input, quality_var

    link_input = ctk.CTkEntry(app, placeholder_text="Insert a YT video/playlist link here")
    link_input.grid(row = 0, column = 0, padx = (20, 8), pady = 20, sticky = "ew")

    download_btn = ctk.CTkButton(app, text = "Download", width = 100, command = on_download)
    download_btn.grid(row = 0, column = 1, padx = (0, 20), pady = 20)

    quality_frame = ctk.CTkFrame(app, fg_color = "transparent")
    quality_frame.grid(row = 1, column = 0, columnspan = 2, padx = 20, sticky = "w")

    quality_label = ctk.CTkLabel(quality_frame, text = "Quality")
    quality_label.pack(side = "left", padx = (0, 8))

    quality_var = ctk.StringVar(value = "192")
    quality_menu = ctk.CTkOptionMenu(quality_frame, values = ["128", "192", "256", "320"], variable = quality_var)
    quality_menu.pack(side = "left")

    app.mainloop()

if __name__ == "__main__":
    main()