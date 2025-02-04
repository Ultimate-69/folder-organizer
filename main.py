import os
import tkinter as tk
from tkinter import filedialog

def main():
    isValidPath = False
    path = ""

    root = tk.Tk()
    root.geometry("400x400")
    root.title("File Organizer")
    root.configure(bg="gray")

    content = tk.Frame(root)
    button = tk.Button(root, text="Organize Folder...", command= lambda: get_directory(root))
    button.pack()

    root.mainloop()

def get_directory(root):
    directory = filedialog.askdirectory()
    if directory != "" and directory != None:
        if os.path.exists(directory):
            print(directory)
            if os.path.isdir(directory):
                organize_folder(directory)
                label = tk.Label(root, text="Successfully Organized!")
                label.pack()
            

def organize_folder(path):
    with os.scandir(path) as files:
        for file in files:

            if os.path.isdir(file):
                if "Files" in file.name or "Folders" in file.name:
                    continue

                folderName = "Folders"
                newPath = os.path.join(path, folderName)
                if os.path.exists(newPath):
                    os.replace(file.path, os.path.join(newPath, file.name))
                else:
                    os.mkdir(newPath)
                    os.replace(file.path, os.path.join(newPath, file.name))
                    
                continue

            fileName, extension = os.path.splitext(file.name)

            folderName = extension.capitalize() + " Files"

            if os.path.exists(os.path.join(path, folderName)):
                newPath = os.path.join(path, folderName)
                os.replace(file.path, os.path.join(newPath, file.name))
            else:
                newPath = os.path.join(path, folderName)
                os.mkdir(newPath)
                os.replace(file.path, os.path.join(newPath, file.name))



if __name__ == "__main__":
    main()