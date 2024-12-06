import tkinter as tk
import os
import shutil
from tkinter import messagebox, filedialog

def sortFolder(folder):
    file_types = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.heic', '.raw', '.ico'],
        'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.3gp', '.mxf'],
        'Audio': ['.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a', '.wma', '.amr', '.aiff'],
        'Document': ['.doc', '.docx', '.pdf', '.txt', '.rtf', '.odt', '.epub', '.ppt', '.pptx', '.xls', '.xlsx', '.csv', '.xml', '.md', '.json', '.key', '.odg', '.ods'],
        'Archives': ['.zip', '.gz', '.tar', '.rar', '.7z', '.iso', '.exe', '.msi', '.xz', '.bz2', '.dmg'],
        'Code': ['.py', '.java', '.cpp', '.js', '.html', '.css', '.php', '.rb', '.go', '.ts', '.json', '.cs', '.bat', '.sh', '.ini'],
        'Fonts': ['.ttf', '.otf', '.woff', '.woff2', '.eot'],
        'Misc': ['.log', '.bak', '.dat', '.md', '.tmp', '.cfg', '.jar', '.crp']
    }

    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1].lower()
            for folder_name, extensions in file_types.items():
                if ext in extensions:
                    target_folder = os.path.join(folder, folder_name)
                    os.makedirs(target_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(target_folder, filename))
                    print(f'Move {filename} to {folder_name} folder')
    messagebox.showinfo("Completed", "Sort completed!")

def selectFolder():
    folder = filedialog.askdirectory(title="Select folder")
    if folder:
        sortFolder(folder)

root = tk.Tk()
root.title("Sort folder")
root.geometry("400x200")

title_label = tk.Label(root, text="Sort file type", font=("Arial", 16))
title_label.pack(pady=20)

select_button = tk.Button(root, text="Select folder", command=selectFolder)
select_button.pack(pady=10)

root.mainloop()