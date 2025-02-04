import os

def main():
    isValidPath = False
    path = ""

    # Gets a valid path from the user
    while not isValidPath:
        try:
            path = input("Please enter the path to the directory: ")
        except ValueError:
            print("Error! Please try again.")
            continue

        isValidPath = os.path.exists(path)
        if not isValidPath:
            print("Not a valid path!")
        elif not os.path.isdir(path):
            print("Please provide a folder, not a file!")
            isValidPath = False

    organize_folder(path)

def organize_folder(path):
    files = os.scandir(path)
    for file in files:

        if os.path.isdir(file):
            if "Files" in file.name:
                continue
            continue

        fileName, extension = os.path.splitext(file.name)
        print(extension)

        folderName = extension.capitalize() + " Files"


if __name__ == "__main__":
    main()