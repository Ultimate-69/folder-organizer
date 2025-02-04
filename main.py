import os
import tkinter as tk

def main():
    isValidPath = False
    path = ""

    root = tk.Tk()
    root.geometry("400x400")
    root.title("File Organizer")
    content = tk.Frame(root)

    root.mainloop()

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