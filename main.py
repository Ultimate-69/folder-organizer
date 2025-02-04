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

    files = os.scandir(path)
    organize_folder(files)

def organize_folder(files):
    for file in files:
        print(file.name)

if __name__ == "__main__":
    main()