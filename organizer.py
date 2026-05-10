import os
import shutil

# Folder path to organize
path = "/mnt/c/users/asus/OneDrive/Desktop/contain"

file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Music": [".mp3"]
}

# Read all files
files = os.listdir(path)
for file in files:

    file_path = os.path.join(path, file)
    if os.path.isdir(file_path):
        continue

    # Get extension
    _, extension = os.path.splitext(file)

    # Check category
    for folder_name, extensions in file_types.items():

        if extension.lower() in extensions:

            # Create folder if not exists
            folder_path = os.path.join(path, folder_name)

            if not os.path.exists(folder_path):
                os.mkdir(folder_path)

            # Move file
            shutil.move(file_path, os.path.join(folder_path, file))

            print(f"Moved {file} -> {folder_name}")

            break

    
