import os
import shutil

# Change this to your Downloads folder
folder = r"C:\Users\godwo\Downloads"

folders = {
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",

    ".pdf": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".xlsx": "Documents",
    ".mp3": "Music",
    ".mp4": "Videos",

    ".zip": "Archives",

    ".csv": "CSV"
}

for file in os.listdir(folder):

    source = os.path.join(folder, file)

    if os.path.isfile(source):

        filename, extension = os.path.splitext(file)

        extension = extension.lower()

        if extension in folders:

            destination = os.path.join(folder, folders[extension])

            os.makedirs(destination, exist_ok=True)

            shutil.move(source, os.path.join(destination, file))

            print(f"Moved: {file} → {folders[extension]}")

print("Organization complete!")