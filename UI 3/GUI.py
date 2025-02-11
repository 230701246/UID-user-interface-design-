
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb  # Modern UI theme
from PIL import Image, ImageTk  # For icons

def rename_file():
    old_name = old_file_entry.get()
    new_name = new_file_entry.get()
    if old_name and new_name:
        status_label.config(text=f'Renamed "{old_name}" to "{new_name}"', foreground="green")
    else:
        status_label.config(text="Please enter both filenames", foreground="red")

root = tb.Window(themename="superhero")  # Stylish theme
root.title("File Renamer")
root.geometry("1000x1000")
root.resizable(False, False)
root.configure(bg="#D1E8E2")  # Light pastel background

title_label = tk.Label(root, text="File Renamer by 230701246", font=("Arial", 20, "bold"), fg="BLACK", bg="#4682B4")
title_label.pack(fill="x", pady=10)


frame = tk.Frame(root, bg="#D1E8E2", padx=20, pady=20)
frame.pack(pady=10)

old_file_label = ttk.Label(frame, text="Old Filename:", font=("Arial", 12, "bold"))
old_file_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

old_file_entry = ttk.Entry(frame, width=25, font=("Arial", 12))
old_file_entry.grid(row=0, column=1, padx=10, pady=10)

new_file_label = ttk.Label(frame, text="New Filename:", font=("Arial", 12, "bold"))
new_file_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

new_file_entry = ttk.Entry(frame, width=25, font=("Arial", 12))
new_file_entry.grid(row=1, column=1, padx=10, pady=10)


rename_button = tb.Button(root, text="Rename File", bootstyle="success", command=rename_file, width=15)
rename_button.pack(pady=15)




icon_img = Image.open("C:\sem 4\PUP.png").resize((1000, 50))  # Add your own icon.png
icon_tk = ImageTk.PhotoImage(icon_img)


title_frame = tk.Frame(root, bg="#4682B4", height=50)
title_frame.pack(fill="x")

icon_label = tk.Label(title_frame, image=icon_tk, bg="#4682B4")
icon_label.pack(side="left", padx=10, pady=5)



status_label = tk.Label(root, text="", font=("Arial", 10), bg="#D1E8E2")
status_label.pack(pady=5)

root.mainloop()



